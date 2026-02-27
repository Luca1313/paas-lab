from dotenv import load_dotenv
from datapizza.pipeline.pipeline import IngestionPipeline

load_dotenv()

pipeline = IngestionPipeline().from_yaml("./src/paas_lab/utils/config_ingestion.yml")
pipeline.run(
    file_path="old-dataset/Hackapizza Dataset/Codice Galattico/Codice Galattico.pdf"
)
