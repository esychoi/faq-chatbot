from FlagEmbedding import BGEM3FlagModel


class BgeM3EmbedddingModel:
    def __init__(self, model_name: str = "BAAI/bge-m3", use_fp16: bool = True):
        self.model = BGEM3FlagModel(model_name, use_fp16=use_fp16)

    def encode_documents(
        self,
        documents: list[str],
        return_dense: bool = True,
        return_sparse: bool = False,
    ):
        return self.model.encode(
            documents,
            batch_size=12,
            max_length=1024,
            return_dense=return_dense,
            return_sparse=return_sparse,
        )["dense_vecs"]
