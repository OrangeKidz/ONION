import google.generativeai as genai
import subprocess

def avoid_code_formatting(code):
    return code.strip('```python').strip('```')

genai.configure(api_key="")

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

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["You're Onion, Onion Is An LNP (Language Natural Programmation) That Can Transform Simple Human Language Into Complex And Advanced Python Code, You're The Python Interpreter, You Don't Have To Say Something, Go Ahead And Just Make The Code Like An Interpreter, Remember, Don't Use Format Block Code, Example: ```python, Don't Use This, Don't Talk In Code Too, Just Follow The Rule: Don't Talk Something, Just Make The Code For Client"]
  },
  {
    "role": "model",
    "parts": ["import random as rand\nimport os\n\nresponse = input(\"The Cake Is A Lie (Y / N): \")\n\nif response == \"Y\" or \"Yes\":\n    print(\"You Win!\")\n\nelse:\n    print(\"You Lose!\")"]
  },
])

while True:
    user_input = input("> ")
    convo.send_message(user_input)

    # Assuming the last message from Onion contains the Python code
    onion_code = convo.last.text

    # Remove code formatting
    onion_code = avoid_code_formatting(onion_code)

    # Save the code to a file
    with open("onion_code.py", "w") as code_file:
        code_file.write(onion_code)

    # Compile and run the code
    try:
        subprocess.run(["python3", "onion_code.py"], check=True)
    except subprocess.CalledProcessError:
        print("Error in running Onion's code")

    # Display Onion's response
    print("Onion:", convo.last.text)