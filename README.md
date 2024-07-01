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

All the above actions will be specified as a program in the main.py file of our 
folder. Based on this our agent will work and perform the tasks given according 
to the instructions

 And one more thing to mention is about how it can perform these tasks and how 
it should respond. So to click at some point it needs to calculate the XY 
coordinates of our system and know the dimensions. And this is the point where 
our LLM(GPT) can’t help us so we need something to calculate this on our 
operating system. So this the point where Gen engineering helps to do this as 
Gen engineering knows which are available for us to help and build these kinds 
of solution


So when it comes to Python there is a library called Pi Auto GUI that performs 
this exact task so we need to install this library in a script that will give all the 
coordinates and also access the keyboard and cursor of the computer. So just by 
connecting this library with GPT-4 vision we can calculate the system
measurements and act accordingly to perform the tasks
