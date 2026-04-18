

import os
from dotenv import load_dotenv
import requests
# Load environment variables from .env file
load_dotenv()

OPENROUTER_API_KEY = os.getenv("API_KEY")
def call_openrouter_api(messages):
    model = "openrouter/free"
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
        json={
            "model": model,
            "messages": messages
        }
    )
    try:
        return response.json()["choices"][0]["message"]["content"]['response']
    except KeyError:
        print("API Response:", response.json())
        print("Error Code:", response.json().get('error').get('code'))
        print("Error: Unexpected API response format")
        raise ValueError("Error: Code:", response.json().get('error').get('code')) 

def record_expense(user_query):
    # load prompt and add user query
    with open("expense_prompt.txt", "r") as f:
        prompt = f.read()
    prompt += f"\nUser Query: {user_query}\n"
    # call the model to get the response
    messages = [
        {"role": "system", "content": prompt}
    ]
    # parse json
    try:
        response = call_openrouter_api(messages)
        print("Model Response:", response)

        response = eval(response)  # Convert string to dictionary
    except Exception as e:
        print("Error parsing response:", e)
        return {"error": "Failed to parse model response " + str(e)}
    print("Parsed Response:", response)
    return response