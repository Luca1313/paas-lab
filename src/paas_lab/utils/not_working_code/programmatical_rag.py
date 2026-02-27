import os
from dotenv import load_dotenv
from datapizza.embedders.cohere import CohereEmbedder
from datapizza.core.vectorstore import VectorConfig
from datapizza.modules.prompt import ChatPromptTemplate
from datapizza.pipeline import DagPipeline

from paas_lab.utils.openai_client import openai_client
from paas_lab.utils.qdrant_db_client import qdrant_vectorstore

load_dotenv()

embedder = CohereEmbedder(
    api_key=os.getenv("COHERE_API_KEY"),
    base_url=os.getenv("COHERE_ENDPOINT"),
    model_name="embed-v4.0",
    input_type="query",
)

retriever = qdrant_vectorstore

retriever.create_collection(
    collection_name="knowledge_base",
    vector_config=[VectorConfig(dimensions=1536, name="vector")],
)

prompt_template = ChatPromptTemplate(
    user_prompt_template="User question: {{user_prompt}}\n:",
    retrieval_prompt_template="Retrieved content:\n{% for chunk in chunks %}{{ chunk.text }}\n{% endfor %}",
)

dag_pipeline = DagPipeline()
dag_pipeline.add_module("embedder", embedder)
dag_pipeline.add_module("retriever", retriever)
dag_pipeline.add_module("prompt", prompt_template)
dag_pipeline.add_module("generator", openai_client)

dag_pipeline.connect("embedder", "retriever", target_key="query_vector")
dag_pipeline.connect("retriever", "prompt", target_key="chunks")
dag_pipeline.connect("prompt", "generator", target_key="memory")

query = "In che data risale il decreto del gran consiglio?"

result = dag_pipeline.run(
    {
        "embedder": {"text": query},
        "prompt": {"user_prompt": query},
        "retriever": {"collection_name": "tutorial_ingestion", "k": 5},
        "generator": {"input": query},
    }
)

print(f"Generated response: {result['generator']}")
