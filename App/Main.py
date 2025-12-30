from fastapi import FastAPI
from App.api.chat_api import Router
app=FastAPI(title='AI ChatBot')

app.include_router(Router)


@app.get("/")
def health():
    return {"status": "Chatbot running"}