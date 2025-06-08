import json

from fastapi import APIRouter, HTTPException, UploadFile

from chatbot.db.vectorstore.milvus import milvus_manager
from chatbot.embeddings import bge_m3

faq_collections_router = APIRouter()


@faq_collections_router.get("/")
def get_collection_list() -> list[str]:
    return milvus_manager.get_collection_list()


@faq_collections_router.post("/", status_code=201)
def post_collection(faq_file: UploadFile) -> dict[str, str]:
    if not faq_file.filename.endswith(".json"):
        raise HTTPException(status_code=400, detail="File must be a JSON file.")

    faq_collection_name = faq_file.filename.split(".")[0]
    if faq_collection_name in milvus_manager.get_collection_list():
        raise HTTPException(
            status_code=400,
            detail=f"Collection '{faq_collection_name}' already exists.",
        )

    contents = json.loads(faq_file.file.read().decode("utf-8"))
    faq_questions_embeddings = bge_m3.encode_documents(
        [item["question"] for item in contents]
    )
    faq_data = [
        {**item, "question_embedding": embedding}
        for item, embedding in zip(contents, faq_questions_embeddings)
    ]

    milvus_manager.add_faq_collection(
        collection_name=faq_collection_name, faq_data=faq_data
    )

    return {"collection_name": faq_collection_name}


@faq_collections_router.delete("/{faq_collection_name}")
def get_collection_list(faq_collection_name: str) -> dict[str, str]:
    if faq_collection_name not in milvus_manager.get_collection_list():
        raise HTTPException(
            status_code=400,
            detail=f"Collection '{faq_collection_name}' does not exist.",
        )
    milvus_manager.delete_faq_collection(faq_collection_name)
    return {"collection_name": faq_collection_name}
