from fastapi import FastAPI
import os
import requests
from dotenv import load_dotenv
import services

app = FastAPI()


@app.get("/")
def home():
    return {"message": "App is live ⭐"}

@app.get("/chat/{query}")
def chat(query: str):
    messages = [
        {"role": "user", "content": query}
    ]
    response = services.call_openrouter_api(messages)
    return {"response": response}

@app.get("/record_expense/{query}")
def record_expense(query: str):
    response = services.record_expense(query)
    return {"response": response}