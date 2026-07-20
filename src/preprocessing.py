# src/preprocessing.py

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Variables categóricas y numéricas
categorical_features = [
    "Contract", "Payment Method", "Internet Service",
    "Online Security", "Tech Support", "Gender"
]
numeric_features = [
    "Tenure Months", "Monthly Charges", "CLTV", "Churn Score"
]

# Preprocesador: OneHot para categóricas + StandardScaler para numéricas
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ("num", StandardScaler(), numeric_features)
    ]
)
