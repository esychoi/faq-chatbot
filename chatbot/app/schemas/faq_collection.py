from pymilvus import CollectionSchema, DataType, FieldSchema

_id = FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True)
_question = FieldSchema(name="question", dtype=DataType.VARCHAR, max_length=256)
_answer = FieldSchema(name="answer", dtype=DataType.VARCHAR, max_length=2048)
_question_embedding = FieldSchema(
    name="question_embedding", dtype=DataType.FLOAT16_VECTOR, dim=1024
)

faq_schema = CollectionSchema(
    fields=[_id, _question, _answer, _question_embedding],
    description="FAQ Collection Schema",
)
