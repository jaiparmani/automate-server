from fastapi import FastAPI
import os
import requests
app = FastAPI()

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
    return response.json()["choices"][0]["message"]["content"]

@app.get("/")
def home():
    return {"message": "App is live ⭐"}

@app.get("/chat/{query}")
def chat(query: str):
    messages = [
        {"role": "user", "content": query}
    ]
    response = call_openrouter_api(messages)
    return {"response": response}