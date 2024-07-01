# AI Software Engineer

This repository contains the implementation of an AI software engineer capable of autonomously writing, finishing, and debugging code. The AI engineer leverages advanced algorithms and machine learning to analyze data, recognize patterns, and make decisions with minimal human intervention.

## Overview

The AI software engineer is designed to assist in various software development tasks, including code generation, bug detection, and debugging. The agent's architecture consists of a large language model, memory, and tools to enhance the workflow of software engineers by automating tasks and improving code quality.

## Key Components

1. **Large Language Model (LLM):** 
   - Core component responsible for understanding natural language, generating code, and making decisions.
   - Utilizes models like GPT-4 Vision, Gemini Pro Vision, Claude 3, and Large Language and Vision Assistant.

2. **Memory (Context Window):** 
   - Stores context and information relevant to the current task, including code snippets, variables, and project-specific details.

3. **Tools:** 
   - Includes utilities to interact with the computer, such as mouse, keyboard, and browser interfaces.

## Repository Structure

- **models/**: Contains code related to different multimodal models used by the framework.
- **utils/**: Holds utility functions and helper scripts for logging, error handling, data manipulation, and screen capture.
- **config.py**: Manages configuration settings for the framework.
- **exceptions.py**: Defines custom exceptions for specific error scenarios.
- **main.py**: Entry point for the application, sets up the environment, processes the screen, and performs actions based on the model's output.

## Getting Started

### Prerequisites

- Python 3.x
- Git


1. **Clone the repository:**
   git clone https://github.com/OthersideAI/self-operating-computer.git

2. **Navigate to the directory:**
    cd self-operating-computer

3. **Create a Python virtual environment:**
    python3 -m venv venv

4. **Activate the virtual environment:**
    source venv/bin/activate  # Linux/macOS
    source venv/Scripts/activate  # Windows

5. **Install dependencies:**
    pip install -r requirements.txt

6. **Create a Python virtual environment:**
    OPENAI_API_KEY="YOUR_OPENAI_API_KEY"

7. **To execute:**
    operate


The self-operating computer will start and will prompt you for commands. You can issue commands using the following format:

CLICK: Click on a specific area on the screen. Example: CLICK{{"x":"50%","y":"60%","description":"Click: Google Search field"}}
TYPE: Type some text. Example: TYPE "https://www.amazon.com/"
SEARCH: Search for an application on Windows. Example: SEARCH "Spotify"
DONE: Signal that the previous task is completed.
