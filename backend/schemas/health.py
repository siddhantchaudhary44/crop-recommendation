from pydantic import BaseModel

class HealthResponse(BaseModel):
    """define the response structure of the health checkpoint"""
    status:str="ok"
    app_name:str
    version:str