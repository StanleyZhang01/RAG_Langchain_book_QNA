from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
import shutil
from dotenv import load_dotenv
import chromadb

CHROMA_PATH = "chroma"
DATA_PATH = "stories/Cinderella.md"

# Load environment variables from .env file
load_dotenv()

def load_document(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def split_text(content: str):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=500,
        length_function=len,
        add_start_index=True
    )
    chunks = text_splitter.split_text(content)
    return chunks

def save_to_chroma(chunks: list[str]):
    # Remove any existing data chroma databases
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)
        os.makedirs(CHROMA_PATH)

    # Initialize Chroma client with persistence
    client = chromadb.PersistentClient(path=CHROMA_PATH)

    # Create or get a collection
    collection = client.get_or_create_collection(
        name = "my_collection", 
        metadata={"hnsw:space": "cosine"}
    )

    # Generate IDs for each chunk
    ids = [f"chunk_{i}" for i in range(len(chunks))]

    # Add chunks to the collection
    collection.add(
        documents=chunks,
        ids=ids
    )

def main():
    documents = load_document(DATA_PATH)
    chunks = split_text(documents)
    save_to_chroma(chunks)  

if __name__ == "__main__":
    main()