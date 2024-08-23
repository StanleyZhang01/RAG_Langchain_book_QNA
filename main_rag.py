import chromadb
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

CHROMA_PATH = "chroma"
PROMPT_TEMPLATE = """
Answer the question based only on the following context:
{context}
 - -
Answer the question based on the above context: {question}
If you can not confidently answer the question based on the context, then say "I don't know"
"""

openai_client = OpenAI()
openai_client.api_key = os.getenv("OPENAI_API_KEY")
client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = client.get_collection(name="my_collection")

def query_rag(query_txt):
    results = collection.query(
        query_texts=query_txt,
        n_results=3,
        include=["documents"]
    )
    return results['documents']

def ask_gpt(prompt):
    completion = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content

def main():
    question = "where did cinderella's carriage come from"
    rag_context = query_rag(question)
    prompt = PROMPT_TEMPLATE.format(context=rag_context, question=question)
    response = ask_gpt(prompt)
    print(response)

if __name__ == "__main__":
    main()