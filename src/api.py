from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"
@app.post("/chat")
async def chat(req: ChatRequest):
    return {"reply": "Hello from AI!", "session": req.session_id}
