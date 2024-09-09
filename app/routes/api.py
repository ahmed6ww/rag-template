from fastapi import APIRouter
from app.models import QueryRequest, DocumentResponse
from app.services.retrieval_service import retrieve_documents
from app.services.generation_service import generate_response

router = APIRouter()

@router.post("/query", response_model=DocumentResponse)
async def query_documents(request: QueryRequest):
    documents = retrieve_documents(request.query)
    return DocumentResponse(documents=documents)

@router.post("/generate", response_model=str)
async def generate_text(request: QueryRequest):
    response = generate_response(request.query)
    return response
