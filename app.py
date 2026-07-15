from flask import Flask, render_template, request
import joblib
import numpy as np


app = Flask(__name__)


# Load ML files
model = joblib.load("models/crop_model.pkl")
scaler = joblib.load("models/scaler.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        N = float(request.form["N"])
        P = float(request.form["P"])
        K = float(request.form["K"])
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        ph = float(request.form["ph"])
        rainfall = float(request.form["rainfall"])

        input_data = np.array(
            [[N, P, K, temperature, humidity, ph, rainfall]]
        )

        input_scaled = scaler.transform(input_data)

        prediction = model.predict(input_scaled)

        crop = label_encoder.inverse_transform(prediction)[0]

        return render_template(
            "result.html",
            prediction=crop
        )

    except Exception as e:
        return render_template(
            "error.html",
            error=e
        )


if __name__ == "__main__":
    app.run(debug=True)