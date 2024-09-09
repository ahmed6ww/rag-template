from typing import List
import gemine

# Initialize the Gemine Flash model
model = gemine.FlashModel()

def chunk_text(text: str, max_chunk_size: int = 500) -> List[str]:
    """
    Chunk the input text into smaller pieces.
    """
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        if len(' '.join(current_chunk + [word])) > max_chunk_size:
            chunks.append(' '.join(current_chunk))
            current_chunk = [word]
        else:
            current_chunk.append(word)

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks

def embed_text(chunks: List[str]) -> List[dict]:
    """
    Embed each chunk of text using the Gemine Flash model.
    """
    embeddings = []
    for chunk in chunks:
        embedding = model.embed(chunk)
        embeddings.append({"chunk": chunk, "embedding": embedding})
    return embeddings

def generate_text(query: str, embeddings: List[dict]) -> str:
    """
    Generate a response using the embeddings and the query.
    """
    context = " ".join([embedding["chunk"] for embedding in embeddings])
    prompt = f"Context: {context}\n\nQuery: {query}\n\nResponse:"
    
    response = model.generate(prompt)
    return response.strip()
