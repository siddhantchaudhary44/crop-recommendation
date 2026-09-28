from pydantic import BaseModel,Field

class UserInput(BaseModel):
    Nitrogen:float=Field(..., description="Nitrogen content in soil")
    Phosphorus:float=Field(..., description="Phosporus content in soil")
    Potassium:float=Field(..., description="Potasium content in soil")
    Temperature:float=Field(..., description="temperature in celcius")
    Humidity:float=Field(..., description="Humidity in celcius")
    pH_Value:float=Field(..., description="Soil pH value")
    Rainfall:float=Field(..., description="Rainfall in mm")