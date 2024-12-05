# Tipado
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document
from typing import TypedDict

# LLM
from langchain_anthropic import ChatAnthropic

# Para el indexing
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_nomic import NomicEmbeddings
from langchain_chroma import Chroma

# Para la generación
from langchain import hub

# Variables de entorno
from os import getenv
from dotenv import load_dotenv

load_dotenv()

CLAUDE_API_KEY = getenv("CLAUDE_API_KEY")
MODEL_NAME = getenv("CLAUDE_MODEL_NAME")
NOMIC_API_KEY = getenv("NOMIC_API_KEY")
LANGCHAIN_API_KEY = getenv("LANGCHAIN_API_KEY")

CHUNK_SIZE = int(getenv("CHUNK_SIZE"))
CHUNK_OVERLAP = int(getenv("CHUNK_OVERLAP"))


class State(TypedDict):
    question: str
    context: list[Document]
    answer: str


llm: ChatAnthropic = ChatAnthropic(
    api_key=CLAUDE_API_KEY,
    model=MODEL_NAME,
    temperature=0,
    max_tokens=2000,
)

text_splitter: RecursiveCharacterTextSplitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
)

embeddings: NomicEmbeddings = NomicEmbeddings(
    model="gte-multilingual-base",
    nomic_api_key=NOMIC_API_KEY
)

vector_store: Chroma = Chroma(embedding_function=embeddings)

prompt: ChatPromptTemplate = hub.pull("rlm/rag-prompt", api_key=LANGCHAIN_API_KEY)

loader: TextLoader = TextLoader("./info.md", "utf-8")
docs = loader.load()
all_splits: list[Document] = text_splitter.split_documents(docs)
store = vector_store.add_documents(all_splits)

# Temporal, después implementar historial de mensajes
def generate(question: str) -> State:
    retrieved_docs = vector_store.similarity_search(question)
    docs_content = "<context>\n\n"
    docs_content += "\n\n".join(f"<context{i+1}>{doc.page_content}</context{i+1}>" 
                               for i, doc in enumerate(retrieved_docs))
    docs_content += "\n\n</context>"

    message_prompt = {"question": question, "context": docs_content}
    messages = prompt.invoke(message_prompt)
    response = llm.invoke(messages)

    output = {
        "question": question,
        "context": retrieved_docs,
        "answer": response.content
    }

    return output
