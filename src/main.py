import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

from src.chain.rag import RagChain

# 환경변수 로드
load_dotenv()

rag = RagChain()
rag_chain = rag.create_chain()

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    response: str

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/chat", response_model=ChatResponse)
async def chat_with_claude(request: ChatRequest):
    response = rag_chain.invoke({
        "question": request.question
    })
    
    print(response)
    
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
