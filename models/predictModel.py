from beanie import Document
from typing import Text


class predictModel(Document):
    class DocumentMeta:
        collection_name = "predicts"

    predict_score: float
    prediction: str
    text: Text
