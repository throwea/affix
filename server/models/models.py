from pydantic import BaseModel

class ChatRequest(BaseModel):
    user_msg: str 
    user_id: str

class ChatResponse(BaseModel):
    response: str
    success: int

