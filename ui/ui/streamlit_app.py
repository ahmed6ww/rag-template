import streamlit as st
import requests

st.title("RAG System")

query = st.text_input("Enter your query:")

if st.button("Retrieve Documents"):
    response = requests.post("http://localhost:8000/query", json={"query": query})
    if response.status_code == 200:
        documents = response.json().get("documents", [])
        for doc in documents:
            st.write(f"Document ID: {doc['id']}")
            st.write(f"Content: {doc['content']}")
    else:
        st.write("Error retrieving documents")

if st.button("Generate Response"):
    response = requests.post("http://localhost:8000/generate", json={"query": query})
    if response.status_code == 200:
        st.write(response.json())
    else:
        st.write("Error generating response")
