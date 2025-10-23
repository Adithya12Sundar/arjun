from flask import Flask, request, jsonify
from model import predict

app = Flask(__name__)

@app.route("/")
def home():
    return "Server is running!"

@app.route("/predict", methods=["POST"])
def make_prediction():
    data = request.json  # expects JSON input list
    result = predict(data)
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
