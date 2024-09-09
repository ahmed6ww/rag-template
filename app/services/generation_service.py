from app.utils.helpers import chunk_text, embed_text, generate_text
from app.services.retrieval_service import retrieve_documents
from app.models import Document

def generate_response(query: str) -> str:
    # Step 1: Retrieve relevant documents
    documents = retrieve_documents(query)
    
    # Step 2: Chunk the documents
    chunks = []
    for doc in documents:
        chunks.extend(chunk_text(doc.content))
    
    # Step 3: Embed the chunks
    embeddings = embed_text(chunks)
    
    # Step 4: Generate a response using the embeddings
    response = generate_text(query, embeddings)
    
    return response
