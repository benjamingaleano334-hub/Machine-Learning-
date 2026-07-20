# train.py

import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# Importar el preprocesador desde preprocessing.py
from preprocessing import preprocessor

# 1. Cargar dataset
df = pd.read_excel(r"C:\Users\Benja\Desktop\ciencia de datos\machine_learning\perdida_clientes\data\Telco_customer_churn.xlsx")


# 2. Definir variables
target = "Churn Value"
categorical_features = [
    "Contract", "Payment Method", "Internet Service",
    "Online Security", "Tech Support", "Gender"
]
numeric_features = [
    "Tenure Months", "Monthly Charges", "CLTV", "Churn Score"
]

X = df[categorical_features + numeric_features]
y = df[target]

# 3. Dividir dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4. Definir modelo Random Forest
rf_model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

# 5. Crear pipeline
pipeline_rf = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", rf_model)
])

# 6. Entrenar
pipeline_rf.fit(X_train, y_train)

# 7. Evaluar
y_pred = pipeline_rf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1:", f1_score(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, pipeline_rf.predict_proba(X_test)[:,1]))

# 8. Guardar modelo entrenado
joblib.dump(pipeline_rf, r"C:\Users\Benja\Desktop\ciencia de datos\machine_learning\perdida_clientes\models\random_forest_churn.pkl")

print("Modelo guardado en models/random_forest_churn.pkl")
