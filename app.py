from flask import Flask, request, jsonify, send_file
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Load model
model = joblib.load("model.sav")
columns = joblib.load("columns.pkl")

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    input_data = pd.DataFrame([data])

    # arrange columns same as training
    input_data = input_data.reindex(columns=columns, fill_value=0)

    prediction = model.predict(input_data)[0]

    result = "Customer Will Churn" if prediction == 1 else "Customer Will Not Churn"

    return jsonify({
        "prediction": int(prediction),
        "result": result
    })

if __name__ == "__main__":
    app.run(port=8000, debug=True)