import joblib
import pandas as pd
from google.cloud import storage
from io import BytesIO

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

model_version="1.0.0"

"""def predict function"""

def predict_output(user_input:dict):
    """predict the crop using input soil and weather features."""
    input_df=pd.DataFrame([user_input])
    input_data=scaler.transform(input_df)
    prediction=model.predict(input_data)
    return prediction[0]