from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from backend.api.api import api_router
from google.cloud import storage
from io import BytesIO
import joblib

#google storage bucket
BUCKET_NAME="crop-reccomendation-models-2026-sid"

#connect to GCS
client=storage.Client()
bucket=client.bucket(BUCKET_NAME)

#download model and scaler from GCS
model_blob=bucket.blob("model.pk1")
scaler_blob=bucket.blob("scaler.pk1")

model=joblib.load(BytesIO(model_blob.download_as_bytes()))
scaler=joblib.load(BytesIO(scaler_blob.download_as_bytes()))


app=FastAPI()

#store loaded model and scaler
app.state.model=model
app.state.scaler=scaler

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def middleware(request: Request, call_next):
    response = await call_next(request)
    return response

app.include_router(api_router)