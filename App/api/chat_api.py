from fastapi import APIRouter
from pydantic import BaseModel
from App.services.chat import chatresponse

Router=APIRouter(prefix='/chat',tags=['chat'])

class ChatRequest(BaseModel):
 message:str

@Router.post('/')
def chat(req:ChatRequest):
    reply=chatresponse(req.message)
    return {'reply':reply}

