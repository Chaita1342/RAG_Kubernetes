import os
from dotenv import load_dotenv


load_dotenv()

class Settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    
    QDRANT_API_KEY= os.getenv("QDRANT_API_KEY")
    QDRANT_COLLECTION = "enterprise_rag"
    QDRANT_URL = os.getenv("QDRANT_CLUSTER_ENDPOINT") 

    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")
    GROQ_MODEL = "llama-3.3-70b-versatile"
    GROQ_FALLBACK_API_KEY= str = os.getenv("GROQ_FALLBACK_API_KEY")


    JINA_API_KEY = os.getenv("JINA_API_KEY")
    JINA_EMBEDDING_MODEL = "jina-embeddings-v3"
    JINA_RERANK_MODEL = "jina-reranker-v3"

    LOGFIRE_TOKEN = os.getenv("LOGFIRE_TOKEN")
    LOGFIRE_BASE_URL = os.getenv("LOGFIRE_BASE_URL")


settings = Settings()