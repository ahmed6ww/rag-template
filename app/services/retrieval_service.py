import os
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import GithubFileLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load environment variables
GITHUB_ACCESS_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")

if not GITHUB_ACCESS_TOKEN:
    raise ValueError("GITHUB_ACCESS_TOKEN environment variable is not set.")

# Loading Github Repo
def load_documents():
    loader = GithubFileLoader(
        repo="MuhammadAmmar24/Langchain",
        branch="main",
        access_token=GITHUB_ACCESS_TOKEN,
        github_api_url="https://api.github.com",
        file_filter=lambda file_path: file_path.endswith(".md"),
    )
    docs = loader.load()
    return docs

# Splitting documents
def split_documents(docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
    splits = text_splitter.split_documents(docs)
    return splits

# Create embeddings and vectorstore
def create_vectorstore(splits):
    embeddings = HuggingFaceEmbeddings()
    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
    return vectorstore

# Retrieve documents
def retrieve_documents(vectorstore, query):
    retriever = vectorstore.as_retriever(
        search_type="similarity_score_threshold", search_kwargs={"score_threshold": 0.2}
    )
    docs = retriever.invoke(query)
    return docs
