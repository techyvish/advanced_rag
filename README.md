# Advanced RAG

![mermaid-flow-1x](https://github.com/user-attachments/assets/f0eb2037-3e87-4e40-bdbd-a726cd350583)

Welcome to the **ReAct Agent Executor** project! This repository leverages LangChain and OpenAI APIs to demonstrate a ReAct (Reason + Act) agent approach for intelligent text generation and interactions.

---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Project Setup](#project-setup)
 - [1. Create `.env` File](#1-create-env-file)
 - [2. Install Packages](#2-install-packages)
 - [3. Open Project in Your Favorite Editor](#3-open-project-in-your-favorite-editor)
3. [Usage](#usage)
4. [Debugging](#debugging)
5. [Contributing](#contributing)
6. [License](#license)

---

## Prerequisites

- **Python 3.8+** (recommended)
- **Poetry** for Python packaging and dependency management.  
  If you haven’t installed Poetry yet, follow the instructions at [Poetry’s official website](https://python-poetry.org/docs/#installation).

---

## Project Setup

### 1. Create `.env` File
In the root directory of the project, create a file named `.env` and add the following environment variables:

```bash
OPENAI_API_KEY=
LANGCHAIN_API_KEY=
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=ReAct agent executor
TAVILY_API_KEY=`` 
```
> **Note:**
> 
> -   Replace the values on the right side of the `=` with your actual keys or desired settings.
> -   If you do not have some of these keys, you can either leave them blank or comment them out.

### 2. Install Packages

From the project’s root directory, run:

`poetry install` 

This command will install all required dependencies listed in `pyproject.toml`.

### 3. Open Project in Your Favorite Editor

Open the project in any editor or IDE of your choice (e.g., VS Code, PyCharm, etc.) for further development or debugging.

## Usage

Once your environment is set up and dependencies are installed, you can run or modify the `main.py` file to interact with the ReAct agent. Typical usage involves:

1.  Ensuring you have the correct environment variables in `.env`.
2.  Activating the Poetry virtual environment:
        
    `poetry shell` 
    
3.  Running the script:
    
    `poetry run python main.py` 
    
    or, if you have already activated the shell:
    
    `python main.py` 
    

----------

## Debugging

-   **VS Code**: Create a `launch.json` in the `.vscode` folder or use the built-in debugging feature. Make sure the Python interpreter is set to the Poetry environment.
-   **PyCharm**: Configure a Python run/debug configuration pointing to `main.py` and set environment variables accordingly.
-   **CLI Debugging**: Use `print()` statements or Python’s built-in `pdb` for simple command-line debugging.

----------

## Contributing

Contributions are welcome! Feel free to open issues or pull requests to improve this project. For major changes, please open an issue first to discuss what you would like to change.

----------

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and use it as per the terms of the license.
