from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model = joblib.load('best_xgb.pkl')

@app.post("/predict/")
def predict(features: list):
    features_array = np.array(features).reshape(1, -1)
    prediction = model.predict(features_array)
    return {"churn prediction": int(prediction[0])}

