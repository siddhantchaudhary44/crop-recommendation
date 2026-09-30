from pydantic import BaseModel,Field

class UserInput(BaseModel):
   
    Nitrogen:float=Field(..., ge=0, le=300, description="Nitrogen content in soil")
    Phosphorus:float=Field(..., ge=5, le=145, description="Phosporus content in soil")
    Potassium:float=Field(..., ge=5, le=205, description="Potasium content in soil")
    Temperature:float=Field(..., ge=-10, le=60, description="temperature in celcius")
    Humidity:float=Field(..., ge=15, le=100, description="Humidity in celcius")
    pH_Value:float=Field(..., ge=3.5, le=10, description="Soil pH value")
    Rainfall:float=Field(..., ge=20.2, le=298.6, description="Rainfall in mm")