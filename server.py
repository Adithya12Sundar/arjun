from flask import Flask, request, jsonify
from model import predict

app = Flask(__name__)

@app.route("/")
def home():
    return "Server is running!"

@app.route("/predict", methods=["POST"])
def make_prediction():
    data = request.json  # expects JSON input list
    result = str(data) + "arjun"
    return jsonify({"prediction": result})
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render gives the port
    app.run(host="0.0.0.0", port=port)        # Listen on all network interfaces


