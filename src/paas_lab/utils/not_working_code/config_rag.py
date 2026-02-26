from dotenv import load_dotenv
from datapizza.pipeline import DagPipeline
#from datapizza.tracing import ContextTracing

load_dotenv()

dag_pipeline = DagPipeline().from_yaml('./src/paas_lab/utils/config_rag.yml')

query = 'In che data risale il decreto del gran consiglio?'

#with ContextTracing().trace('dag_pipeline'):
result = dag_pipeline.run(
    {
        'embedder': {'text': query},
        'prompt': {'user_prompt': query},
        'retriever': {
            'collection_name': 'tutorial_ingestion',
            'k': 5
        },
        'generator': {'input': query}
    }
)

print(f'Generated response: {result['generator']}')