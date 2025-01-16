from dotenv import load_dotenv

from langgraph.graph import END, StateGraph
from graph.const import RETRIEVE, GRADE_DOCUMENTS, GENERATE, WEBSEARCH
from graph.nodes import generate, grade_documents, retrieve, web_search
from graph.state import GraphState
from graph.chains.answer_grader import answer_grader
from graph.chains.hallucination_grader import hallucination_grader
from graph.chains.router import question_router, RouteQuery

load_dotenv()


def grade_generation_grounded_in_documents_and_question(state: GraphState) -> str:
    question = state["question"]
    document = state["documents"]
    generation = state["generation"]

    score = hallucination_grader.invoke(
        {"documents": document, "generation": generation}
    )

    if hallucination_grade := score.binary_score:
        print("---DECISION: GENERATION IS GROUNDED IN DOCUMENTS?---")
        print("---GRADE GENERATION vs QUESTION --- ")
        score = answer_grader.invoke({"question": question, "generation": generation})
        if answer_grade := score.binary_score:
            print("---DECISION: GENERATION ADDRESSES QUESTION---")
            return "useful"
        else:
            print("---DECISION: GENERATION DOES NOT ADDRESSES QUESTION---")
            return "not useful"
    else:
        print("---DECISION: GENERATION IS NOT GROUNDED IN DOCUMENTS---")
        return "not supported"


def decide_to_generate(state):
    if state["web_search"]:
        return WEBSEARCH
    else:
        return GENERATE


def route_question(state: StateGraph) -> str:
    print("---ROUTE QUESTION--- ")
    question = state["question"]
    source: RouteQuery = question_router.invoke({"question": question})
    if source.datasource == "websearch":
        print("---ROUTE QUESTION TO WEB SEARCH---")
        return "websearch"
    elif source.datasource == "vectorstore":
        print("---ROUTE QUESTION TO RAG---")
        return "vectorstore"


workflow = StateGraph(GraphState)

workflow.set_conditional_entry_point(route_question,
                                     path_map={
                                         "websearch": WEBSEARCH,
                                         "vectorstore": RETRIEVE
                                     })

workflow.add_node(RETRIEVE, retrieve)
workflow.add_node(GRADE_DOCUMENTS, grade_documents)
workflow.add_node(GENERATE, generate)
workflow.add_node(WEBSEARCH, web_search)

# workflow.set_entry_point(RETRIEVE)

workflow.add_edge(RETRIEVE, GRADE_DOCUMENTS)
workflow.add_conditional_edges(GRADE_DOCUMENTS,
                               decide_to_generate)

workflow.add_edge(WEBSEARCH, GENERATE)
workflow.add_edge(GENERATE, END)

workflow.add_conditional_edges(
    GENERATE,
    grade_generation_grounded_in_documents_and_question,
    path_map={
        "not supported": GENERATE,
        "useful": END,
        "not useful": WEBSEARCH
    }
)

app = workflow.compile()


print(app.get_graph().draw_mermaid())
