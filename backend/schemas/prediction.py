from pydantic import BaseModel

class Predictionresponse(BaseModel):
    """define the response structure of crop """
    crop:str
