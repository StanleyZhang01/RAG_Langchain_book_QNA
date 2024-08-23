# Overview
Using RAG to ask questions about a book.
The scripts sets up a Chroma vector database for storing text chunks.
It queries them using OpenAI's GPT model for context-based question answering.

## Installation
1. Clone the repository
2. Create a virtual environment
  - python -m venv venv
4. Activate the virtual environment:
  - On Windows:
    ```
    venv\Scripts\activate
    ```
  - On macOS and Linux:
    ```
    source venv/bin/activate
    ```
4. Install the required packages:
  - pip install -r requirements.txt
5. Update the .env file with you open ai API key
  - OPENAI_API_KEY=your-openai-api-key-here
6. Run this script first to generate the data store:
  - python generate_data_store.py
7. Run this script first to ask a question about your book.
  - python ask_qna.py
