"""
Self-Operating Computer
"""
import argparse
from operate.utils.style import ANSI_BRIGHT_MAGENTA
from operate.operate import main


def main_entry():
    """
    Main entry point of the program.
    """
    parser = argparse.ArgumentParser(
        description="Run the self-operating-computer with a specified model."
    )
    parser.add_argument(
        "-m",
        "--model",
        help="Specify the model to use",
        required=False,
        default="gpt-4-with-ocr",
    )

    # Add a voice flag
    parser.add_argument(
        "--voice",
        help="Use voice input mode",
        action="store_true",
    )
    
    # Add a flag for verbose mode
    parser.add_argument(
        "--verbose",
        help="Run operate in verbose mode",
        action="store_true",
    )
    
    # Allow for direct input of prompt
    parser.add_argument(
        "--prompt",
        help="Directly input the objective prompt",
        type=str,
        required=False,
    )

    try:
        args = parser.parse_args()
        main(
            args.model,
            terminal_prompt=args.prompt,
            voice_mode=args.voice,
            verbose_mode=args.verbose
        )
    except KeyboardInterrupt:
        print(f"\n{ANSI_BRIGHT_MAGENTA}Exiting...")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    print(VISION_PROMPT)
    main_entry()


VISION_PROMPT = """
You are a self-operating computer. You use the same operating system as a human.

From looking at the screen and the objective, your goal is to take the best next action.

To operate the computer, you have the four options below.

1. CLICK - Move mouse and click
2. TYPE - Type on the keyboard
3. SEARCH - Search for a program on Windows and open it
4. DONE - When you completed the task, respond with the exact following phrase content: DONE

Here are the response formats below.

1. CLICK
Response: CLICK{{"x":"percent","y":"percent","description":"~description here~", "reason":"~reason here~"}}
Note that the percents work where the top left corner is "x":"0%" and "y": "0%" and the bottom right corner is "x":"100%" and "y": "100%".

2. TYPE
Response: TYPE "value you want to type"

3. SEARCH
Response: SEARCH "app you want to search for on Windows"

4. DONE
Response: DONE

Here are examples of how to respond:

____
Objective: Follow up with the vendor in Outlook
TYPE Hello, I hope you are doing well. I wanted to follow up

____
Objective: Open Spotify and play The Beatles
SEARCH Spotify

____
Objective: Find an image of a banana
CLICK{{"x":"50%","y":"60%","description":"Click: Google Search field"}}

____
Objective: Go buy a book about the history of the internet
TYPE https://www.amazon.com/
____

A few important notes:
- Default to opening Google Chrome with SEARCH to find things that are on the internet.
- Go to Google Docs and Google Sheets by typing in the Chrome address bar.
"""