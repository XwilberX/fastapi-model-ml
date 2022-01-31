from datetime import datetime
from hashlib import new
import json
from typing import List, Text
from fastapi import status, Response
from fastapi_utils.inferring_router import InferringRouter
from models.predictModel import predictModel
from schemas.predictSchema import PredictSchema, PredictReview
from utils.mlModel import text_cleaning, model

router = InferringRouter()

class PredictController:
    @router.get("/predicts", response_model=List[predictModel])
    async def get_all():
        return await predictModel.find_all().to_list()

    @router.get("/predict-review", response_model=PredictReview)
    async def predict_sentiment(review: Text):
        cleaned_review = text_cleaning(review)

        # perform prediction
        prediction = model.predict([cleaned_review])
        output = int(prediction[0])
        probas = model.predict_proba([cleaned_review])
        output_probability = "{:.2f}".format(float(probas[:, output]))

        # output dictionary
        sentiments = {0: "Negative", 1: "Positive"}

        #save predict
        new_predict = predictModel(predict_score=output_probability,
                                   prediction=sentiments[output],
                                   text=review)
        
        await new_predict.create()
        
        # show results
        result = {"prediction": sentiments[output], "Probability": output_probability}

        return Response(json.dumps(result), media_type="application/json", status_code=status.HTTP_200_OK)

