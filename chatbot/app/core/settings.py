import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

project_directory = Path(__file__).parent.parent.parent
dotenv_path = project_directory / ".env"
if dotenv_path.exists():
    load_dotenv()


class Settings(BaseSettings):
    MILVUS_URI: str = os.getenv("MILVUS_URI", "http://localhost:19530")
    MILVUS_TOKEN: str = os.getenv("MILVUS_TOKEN", "root:Milvus")
    MILVUS_DB_NAME: str = os.getenv("MILVUS_DB_NAME", "faq")

    LOGGER_PATH: Path = project_directory / "chatbot" / "app" / "server.log"


settings = Settings()
