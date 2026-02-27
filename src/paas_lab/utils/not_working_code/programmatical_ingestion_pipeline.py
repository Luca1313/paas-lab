import os
from dotenv import load_dotenv
from datapizza.embedders import ChunkEmbedder
from datapizza.embedders.cohere import CohereEmbedder
from datapizza.modules.parsers.docling import DoclingParser
from datapizza.modules.splitters import RecursiveSplitter
from datapizza.core.vectorstore import VectorConfig
from datapizza.pipeline.pipeline import IngestionPipeline

from paas_lab.utils.qdrant_db_client import qdrant_vectorstore

load_dotenv()

parser = DoclingParser()
splitter = RecursiveSplitter(max_char=2000, overlap=100)
embedder = ChunkEmbedder(
    client=CohereEmbedder(
        api_key=os.getenv("COHERE_API_KEY"),
        base_url=os.getenv("COHERE_ENDPOINT"),
        model_name="embed-v4.0",
        input_type="search_document",
    ),
    embedding_name="embedding_vector",
)

qdrant_vectorstore.create_collection(
    collection_name="tutorial_ingestion",
    vector_config=[VectorConfig(dimensions=1536, name="embedding_vector")],
)

pipeline = IngestionPipeline(
    modules=[parser, splitter, embedder],
    vector_store=qdrant_vectorstore,
    collection_name="tutorial_ingestion",
)

pipeline.run(
    file_path="old-dataset/Hackapizza Dataset/Codice Galattico/Codice Galattico.pdf"
)
