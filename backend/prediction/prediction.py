import joblib
import pandas as pd

"""def predict function"""

def predict_output(user_input:dict,model,scaler):
    """predict the crop using input soil and weather features."""
    input_df=pd.DataFrame([user_input])
    input_data=scaler.transform(input_df)
    prediction=model.predict(input_data)
    return prediction[0]