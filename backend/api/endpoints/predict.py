from fastapi import APIRouter, Request
from backend.schemas.user_input import UserInput
from backend.schemas.prediction import Predictionresponse
from backend.prediction.prediction import predict_output

router=APIRouter()

@router.post("/crop-predict",response_model=Predictionresponse)
async def predict(data: UserInput,request:Request):
    """return the predicted crop"""
    input_data=data.model_dump()#Converting in python dictionary
    model=request.app.state.model
    scaler=request.app.state.scaler
    prediction=predict_output(input_data,model,scaler)
    return{
        "crop": prediction
    }