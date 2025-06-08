# faq-chatbot

<p align="center">
    <a href="https://www.python.org/downloads/release/python-31017/" target="_blank">
        <img src="https://img.shields.io/badge/Python-3.10.17-blue?logo=python"
    </a>
    <a href="https://fastapi.tiangolo.com/" target="_blank">
        <img src="https://img.shields.io/badge/fastapi-black?logo=fastapi">
    </a>
    <a href="https://milvus.io/" target="_blank">
        <img src="https://img.shields.io/badge/milvus-black?logo=milvus">
    </a>
</p>

Chatbot answering FAQs.

## Install dependencies

1. Install uv. \
`$ curl -LsSf https://astral.sh/uv/install.sh | sh`
2. Install packages. \
`$ uv sync`

## Setup Milvus

Run the Milvus docker container: \
`$ bash standalone_embed.sh start`

You can access the Milvus WebUI at http://127.0.0.1:9091/webui/. \
Check https://milvus.io/docs/install_standalone-docker.md for more details.

## Launch the API

1. Go to the `chatbot/app/` directory. \
`cd chatbot/app`
2. Run the server. \
`uv run fastapi dev`

The server is running at `http://127.0.0.1:8000`. \
You can check the API documentation at `http://127.0.0.1:8000/docs`

## Environment variables
`.env` example:

```
MILVUS_URI=http://localhost:19530
MILVUS_TOKEN=root:Milvus
MILVUS_DB_NAME="faq"
```