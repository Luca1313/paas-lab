from qdrant_client import QdrantClient
import os
from dotenv import load_dotenv
from datapizza.vectorstores.qdrant import QdrantVectorstore

load_dotenv()

USE_LOCAL = os.getenv("USE_LOCAL_QDRANT", "true") == "true"

if USE_LOCAL:
    qdrant_client = QdrantClient(
        host="localhost",
        port=6333
    )
    qdrant_vectorstore = QdrantVectorstore(
        host="localhost",
        port=6333
    )
else:
    qdrant_client = QdrantClient(
        url=os.getenv("QDRANT_CLUSTER_ENDPOINT"),
        api_key=os.getenv("QDRANT_API_KEY"),
    )
    qdrant_vectorstore = QdrantVectorstore(
        url=os.getenv("QDRANT_CLUSTER_ENDPOINT"),
        api_key=os.getenv("QDRANT_API_KEY"),
    )