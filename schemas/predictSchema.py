from msilib.schema import Class
from pydantic import BaseModel
from typing import List, Text
from datetime import datetime

class PredictSchema(BaseModel):
    predict_score: float
    prediction: str
    text: Text

class PredictListSchema(BaseModel):
    predicts: List[PredictSchema] = []

class PredictReview(BaseModel):
    prediction: Text
    predict_score: float