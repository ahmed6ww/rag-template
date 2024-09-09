from pydantic import BaseModel

class QueryRequest(BaseModel):
    query: str

class Document(BaseModel):
    id: str
    content: str

class DocumentResponse(BaseModel):
    documents: list[Document]
