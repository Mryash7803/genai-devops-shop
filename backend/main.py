from fastapi import FastAPI
from pydantic import BaseModel
import vertexai
from vertexai.generative_models import GenerativeModel
import os

app = FastAPI()

# Initialize Vertex AI
# Using Environment Variable for Project ID is best practice
PROJECT_ID = os.environ.get("GCP_PROJECT_ID", "dogwood-channel-478619-p7")
vertexai.init(project=PROJECT_ID, location="us-central1")

class ChatRequest(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    return {"message": "GenAI Microservice (Gemini) is Running!"}

@app.post("/generate")
def generate_text(request: ChatRequest):
    """
    Calls Google Vertex AI (Gemini Pro) to generate text
    """
    try:
        # Load the Gemini Pro model
        model = GenerativeModel("gemini-2.5-pro")
        
        # Generate content
        response = model.generate_content(request.prompt)
        
        return {"response": response.text}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
