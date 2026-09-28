from fastapi import APIRouter

from backend.schemas.user_input import UserInput
from backend.schemas.prediction import Predictionresponse
from backend.prediction.prediction import predict_output

router=APIRouter()

@router.post("/predict",response_model=Predictionresponse)
async def predict(data: UserInput):
    """return the predicted crop"""
    input_data=data.model_dump()#Converting in python dictionary
    prediction=predict_output(input_data)
    return{
        "crop": prediction
    }