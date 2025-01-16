from typing import Any, Dict
from graph.chains.document_generation import document_generation_chain
from graph.state import GraphState


def generate(state: GraphState) -> Dict[str, Any]:
    print("---GENERATE DOCUMENTS----")

    question = state["question"]
    documents = state["documents"]

    generation = document_generation_chain.invoke({"context": documents, "question": question})
    return {"documents": documents, "question": question, "generation": generation}
