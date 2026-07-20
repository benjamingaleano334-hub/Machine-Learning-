# main.py

from flask import Flask, request, jsonify
from src.predict import predict_churn

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "API de predicción de churn funcionando. Usa /predict con POST."

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    result = predict_churn(data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)

