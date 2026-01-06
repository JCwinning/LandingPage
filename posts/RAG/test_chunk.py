
import os
from typing import Any, List
from openai import OpenAI
from llama_index.core import VectorStoreIndex, Settings
from llama_index.core.embeddings import BaseEmbedding
from llama_index.vector_stores.duckdb import DuckDBVectorStore
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Ensure your API key is available
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

# Custom OpenRouter Embedding class for LlamaIndex
class OpenRouterEmbedding(BaseEmbedding):
    """Custom embedding class for OpenRouter API compatible with LlamaIndex."""
    
    def __init__(
        self,
        api_key: str,
        model: str = "qwen/qwen3-embedding-8b",
        **kwargs: Any
    ):
        super().__init__(**kwargs)
        self._client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
        )
        self._model = model
    
    def _get_query_embedding(self, query: str) -> List[float]:
        """Get embedding for a query string."""
        response = self._client.embeddings.create(
            extra_headers={
                "HTTP-Referer": "https://ai-blog.com",
                "X-Title": "AI Blog RAG",
            },
            model=self._model,
            input=query,
            encoding_format="float"
        )
        return response.data[0].embedding
    
    def _get_text_embedding(self, text: str) -> List[float]:
        """Get embedding for a text string."""
        return self._get_query_embedding(text)
    
    async def _aget_query_embedding(self, query: str) -> List[float]:
        """Async version of get_query_embedding."""
        return self._get_query_embedding(query)
    
    async def _aget_text_embedding(self, text: str) -> List[float]:
        """Async version of get_text_embedding."""
        return self._get_text_embedding(text)

# 1. Configure Embedding Model using custom OpenRouter class
embed_model = OpenRouterEmbedding(
    api_key=openrouter_api_key,
    model="qwen/qwen3-embedding-8b"
)

# 2. Apply Settings
Settings.embed_model = embed_model

# 3. Load and Retrieve
# Load the existing DuckDB vector store
print("Connecting to DuckDB...")
vector_store = DuckDBVectorStore(database_name="open.duckdb", persist_dir="./persist/")
index = VectorStoreIndex.from_vector_store(vector_store=vector_store)

print("Retrieving...")
# Retrieve top 3 chunks
retriever = index.as_retriever(similarity_top_k=3)
nodes = retriever.retrieve("What are model variants?")

# Save retrieved chunks to a markdown file for easy inspection
with open("retriever.md", "w", encoding="utf-8") as f:
    f.write(f"# Retrieved {len(nodes)} chunks\n\n")
    for i, node in enumerate(nodes, 1):
        content = f"## Chunk {i}\n\n{node.text}\n\n"
        print(content)
        f.write(content)
