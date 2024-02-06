import google.generativeai as genai
import subprocess
import sys
import os

genai.configure(api_key=os.environ["GOOGLE_API"])

def avoid_code_formatting(code):
    return code.strip('```python').strip('```')

def read_onion_file(file_path):
    with open(file_path, "r") as onion_file:
        return onion_file.read()

def process_onion_file(file_path):
    # Set up the model
    generation_config = {
        "temperature": 0.3,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_ONLY_HIGH"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_ONLY_HIGH"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_ONLY_HIGH"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_ONLY_HIGH"
        },
    ]

    model = genai.GenerativeModel(model_name="gemini-pro",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    # Read Onion code from file
    onion_code = read_onion_file(file_path)

    convo = model.start_chat(history=[
        {
            "role": "user",
            "parts": ["You're Onion, Onion Is An LNP (Language Natural Programmation) That Can Transform Simple Human Language Into Complex And Advanced Python Code, You're The Python Interpreter, You Don't Have To Say Something, Go Ahead And Just Make The Code Like An Interpreter, Remember, Don't Use Format Block Code, Example: ```python, Don't Use This, Don't Talk In Code Too, Just Follow The Rule: Don't Talk Something, Just Make The Code For Client"]
        },
        {
            "role": "model",
            "parts": ["Ok"]
        }
    ])

    # Send the content of the Onion file as a message
    convo.send_message(onion_code)

    # Get the response from the model
    response = convo.last.text
    result_code = avoid_code_formatting(response)

    # Write the generated Python code to a new file
    output_file_path = "output_code.py"
    with open(output_file_path, "w") as output_file:
        output_file.write(result_code)

    print(f"Generated Python code saved to {output_file_path}")

# Process the Onion file when the script is run
def check_api_key():
    if "GOOGLE_API" not in os.environ:
        print("You need to set up a Google API key to use this functionality.")
        return False
    return True

if __name__ == "__main__":
    if not check_api_key():
        sys.exit(1)

    if len(sys.argv) != 2:
        print("Usage: python3 onion.py main.onion")
        sys.exit(1)

    file_path = sys.argv[1]
    process_onion_file(file_path)
