from visa.pipeline.training_pipeline import TrainingPipeline
from dotenv import load_dotenv
load_dotenv()
pipeline=TrainingPipeline()
pipeline.run_pipeline()
