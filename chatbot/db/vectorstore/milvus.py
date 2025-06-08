from typing import Any

import numpy as np
from pymilvus import MilvusClient

from chatbot.app.core.settings import settings
from chatbot.app.schemas.faq_collection import faq_schema


# TODO: add decorator to check if collection exists
class MilvusManager:
    def __init__(self, uri: str, token: str, db_name: str = "faq"):
        _client = MilvusClient(uri=uri, token=token)
        if db_name not in _client.list_databases():
            _client.create_database(db_name=db_name)
        self.client = MilvusClient(uri=uri, token=token, db_name=db_name)

    def get_collection_list(self) -> list[str]:
        """Get a list of all collections in the Milvus database."""
        return self.client.list_collections()

    def add_faq_collection(
        self, faq_collection_name: str, faq_data: list[dict[str, Any]]
    ):
        """Add a FAQ collection to Milvus. Assumes the collection does not already exist."""
        _index_params = self.client.prepare_index_params()

        _index_params.add_index(
            field_name="question_embedding",
            index_name="question_embedding_index",
            index_type="AUTOINDEX",
            metric_type="L2",
        )
        self.client.create_collection(
            collection_name=faq_collection_name,
            schema=faq_schema,
            index_params=_index_params,
        )
        self.client.insert(collection_name=faq_collection_name, data=faq_data)

    def delete_faq_collection(self, faq_collection_name: str):
        """Delete a FAQ collection from Milvus."""
        self.client.drop_collection(collection_name=faq_collection_name)

    def search(
        self,
        faq_collection_name: str,
        query_embedding: np.ndarray,
        metric_type: str = "L2",
        limit: int = 10,
    ):
        """Conducts vector similarity search in a FAQ collection."""
        search_params = {
            "metric_type": metric_type,
        }
        results = self.client.search(
            collection_name=faq_collection_name,
            data=query_embedding,
            anns_field="question_embedding",
            search_params=search_params,
            output_fields=["id", "question", "answer"],
            limit=limit,
        )
        return results


milvus_manager = MilvusManager(
    uri=settings.MILVUS_URI,
    token=settings.MILVUS_TOKEN,
    db_name=settings.MILVUS_DB_NAME,
)
