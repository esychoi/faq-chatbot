from fastapi import FastAPI

from chatbot.app.routers.faq_collections import faq_collections_router
from chatbot.app.routers.faq_query import faq_query_router

app = FastAPI()
app.include_router(
    faq_collections_router, prefix="/faq_collections", tags=["FAQ Collections CRUD"]
)
app.include_router(faq_query_router, prefix="/search", tags=["FAQ Collections Search"])


@app.get("/")
def read_root() -> str:
    return "Welcome to the Python FAQ Chatbot API!"
