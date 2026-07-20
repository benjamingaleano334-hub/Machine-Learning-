# src/predict.py

import joblib
import pandas as pd

# Cargar modelo entrenado
model = joblib.load(r"C:\Users\Benja\Desktop\ciencia de datos\machine_learning\perdida_clientes\models\random_forest_churn.pkl")

def predict_churn(data: dict):
    """
    Recibe un diccionario con los datos de un cliente y devuelve la predicción.
    Ejemplo de 'data':
    {
        "Contract": "Month-to-month",
        "Payment Method": "Electronic check",
        "Internet Service": "Fiber optic",
        "Online Security": "No",
        "Tech Support": "No",
        "Gender": "Female",
        "Tenure Months": 12,
        "Monthly Charges": 70.35,
        "CLTV": 2500,
        "Churn Score": 65
    }
    """
    df = pd.DataFrame([data])  # convertir a DataFrame
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]
    return {
        "churn_prediction": int(prediction),
        "churn_probability": float(probability)
    }
