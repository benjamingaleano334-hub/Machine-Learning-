# app.py
import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import plotly.graph_objects as go

# Configuración general
st.set_page_config(page_title="Dashboard Churn", layout="wide")

# Barra superior corporativa
st.markdown("""
<style>
.top-bar {
    background-color: #0A74DA;
    padding: 15px;
    color: white;
    font-size: 22px;
    font-weight: bold;
}
.section {
    margin-top: 30px;
}
.card {
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
}
</style>
<div class="top-bar">🔷 Proyecto de Predicción de Pérdida de Clientes</div>
""", unsafe_allow_html=True)

# Menú principal
menu = st.selectbox("Secciones", ["Inicio", "Predicción", "Dashboard", "Modelos"])

# Inicio
if menu == "Inicio":
    st.header("Bienvenido al Proyecto de Churn")
    st.write("""
    Este proyecto busca identificar clientes en riesgo de abandono (churn).
    El churn impacta directamente en los ingresos de la empresa, por lo que anticiparlo
    permite diseñar estrategias de retención más efectivas.
    """)

    col1, col2, col3 = st.columns(3)
    col1.metric("Precisión", "93%")
    col2.metric("Recall", "88%")
    col3.metric("ROC-AUC", "97%")

    st.subheader("Objetivo del Proyecto")
    st.write("""
    - Predecir qué clientes tienen mayor probabilidad de abandonar la empresa.
    - Proporcionar herramientas visuales para empleados que gestionan la relación con clientes.
    - Justificar la elección del modelo Random Forest por su mejor equilibrio entre métricas.
    """)

    st.subheader("Impacto en el último año")
    df = pd.read_excel(r"C:\Users\Benja\Desktop\ciencia de datos\machine_learning\perdida_clientes\data\Telco_customer_churn.xlsx")
    churn_rate = df["Churn Value"].mean()
    st.metric("Pérdida de clientes anual", f"{churn_rate:.2%}")

# Predicción
elif menu == "Predicción":
    st.header("Predicción de Churn")
    st.write("Complete el formulario con los datos del cliente:")

    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    payment = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])
    internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    tenure = st.slider("Tenure Months", 0, 72, 12)
    charges = st.number_input("Monthly Charges", 0.0, 150.0, 70.35)
    cltv = st.number_input("CLTV", 0.0, 10000.0, 2500.0)
    churn_score = st.slider("Churn Score", 0, 100, 65)

    if st.button("Predecir"):
        data = {
            "Contract": contract,
            "Payment Method": payment,
            "Internet Service": internet,
            "Online Security": "No",
            "Tech Support": "No",
            "Gender": "Female",
            "Tenure Months": tenure,
            "Monthly Charges": charges,
            "CLTV": cltv,
            "Churn Score": churn_score
        }
        response = requests.post("http://127.0.0.1:5000/predict", json=data)
        result = response.json()

        st.success(f"Resultado: {'Se va' if result['churn_prediction'] == 1 else 'Se queda'}")
        st.write(f"Probabilidad de churn: {result['churn_probability']:.2%}")

        # Gauge chart
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=result['churn_probability']*100,
            title={'text': "Probabilidad de Churn"},
            gauge={'axis': {'range': [0, 100]},
                   'bar': {'color': "red" if result['churn_prediction'] == 1 else "green"},
                   'steps': [
                       {'range': [0, 30], 'color': "lightgreen"},
                       {'range': [30, 70], 'color': "yellow"},
                       {'range': [70, 100], 'color': "red"}]}))
        st.plotly_chart(fig, use_container_width=True)

# Dashboard
elif menu == "Dashboard":
    st.header("Dashboard de Churn")
    df = pd.read_excel(r"C:\Users\Benja\Desktop\ciencia de datos\machine_learning\perdida_clientes\data\Telco_customer_churn.xlsx")

    churn_rate = df["Churn Value"].mean()
    st.metric("Pérdida de clientes anual", f"{churn_rate:.2%}")

    st.subheader("Churn por tipo de contrato")
    fig_contract = px.bar(df.groupby("Contract")["Churn Value"].mean().reset_index(),
                          x="Contract", y="Churn Value", title="Churn por tipo de contrato")
    st.plotly_chart(fig_contract, use_container_width=True)

    st.subheader("Distribución de clientes")
    fig_dist = px.pie(df, names="Contract", title="Distribución de clientes por contrato")
    st.plotly_chart(fig_dist, use_container_width=True)

# Modelos
elif menu == "Modelos":
    st.header("Comparación de Modelos")
    results = pd.DataFrame({
        "Modelo": ["Logistic Regression", "Random Forest", "XGBoost"],
        "Accuracy": [0.915, 0.932, 0.919],
        "Precision": [0.827, 0.866, 0.840],
        "Recall": [0.858, 0.880, 0.858],
        "F1": [0.843, 0.873, 0.849],
        "ROC-AUC": [0.973, 0.971, 0.977]
    })
    st.dataframe(results)

    st.subheader("Comparación visual")
    st.bar_chart(results.set_index("Modelo")[["Accuracy", "F1", "ROC-AUC"]])

    st.info("Se eligió **Random Forest** por su mejor equilibrio entre todas las métricas.")
