
# Telco Customer Churn Prediction

Proyecto end-to-end de **Machine Learning** para predecir la pérdida de clientes (churn) en una empresa de telecomunicaciones.  
Incluye exploración de datos, preprocesamiento, entrenamiento de modelos, evaluación con métricas y una interfaz gráfica con **Flask** y **Streamlit**.

---

## 📂 Estructura del proyecto

- `data/` → dataset Telco Customer Churn  
- `notebooks/` → análisis exploratorio y modelado  
- `src/` → código fuente (preprocesamiento, entrenamiento, evaluación)  
- `models/` → modelos entrenados guardados con `joblib`  
- `app.py` → aplicación Flask para predicciones  
- `streamlit_app.py` → dashboard interactivo en Streamlit  

---

## ⚙️ Flujo del proyecto

1. **Exploración de datos (EDA)**  
   - Análisis de variables categóricas y numéricas  
   - Visualización de distribución de churn  

2. **Preprocesamiento**  
   - `ColumnTransformer` con `OneHotEncoder` y `StandardScaler`  
   - Pipeline integrado para cada modelo  

3. **Modelado y evaluación**  
   - Modelos: Logistic Regression, Random Forest, XGBoost  
   - Métricas: Accuracy, Precision, Recall, F1, ROC-AUC  
   - Comparación justa con predicciones binarias (`ROC-AUC ≈ 91%`)  
   - Evaluación detallada con probabilidades (`ROC-AUC ≈ 97%`)  

4. **Interfaz gráfica**  
   - Flask API para predicciones  
   - Streamlit dashboard con inputs interactivos  

---

## 📊 Resultados principales

- **Random Forest** seleccionado como mejor modelo.  
- Métricas en test set:  
  - Accuracy: 93%  
  - Precision: 86%  
  - Recall: 88%  
  - F1: 87%  
  - ROC-AUC: 91% (binario), hasta 97% (probabilidades).  

---

## 🚀 Cómo usarlo

### 1. Clonar el repositorio
```bash
git clone https://github.com/tuusuario/telco-churn-prediction.git
cd telco-churn-prediction
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecutar la app con Streamlit
```bash
streamlit run streamlit_app.py
```
Esto abrirá el dashboard en tu navegador, donde podrás ingresar datos de un cliente (contrato, método de pago, servicio de internet, tenure, cargos mensuales, CLTV, churn score) y obtener la predicción.

### 4. Ejecutar la API con Flask
```bash
python app.py
```
Esto levanta un servidor local que recibe peticiones de predicción vía JSON.

---

## 📌 Conclusiones

- El modelo Random Forest logra un excelente equilibrio entre precisión y recall.  
- Detecta clientes en riesgo de churn con alta sensibilidad.  
- El dashboard en Streamlit facilita el uso del modelo en un entorno corporativo.  

