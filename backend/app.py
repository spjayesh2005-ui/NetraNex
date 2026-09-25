from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import io
from services.prediction import demo_predict

app = Flask(__name__)
CORS(app)

ALLOWED_TYPES = {"image/jpeg", "image/png", "image/jpg"}

@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "service": "NetraNexAI API"})

@app.post("/api/screen")
def screen():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    uploaded = request.files["image"]

    if uploaded.mimetype not in ALLOWED_TYPES:
        return jsonify({"error": "Please upload a JPG or PNG fundus image"}), 400

    try:
        image = Image.open(io.BytesIO(uploaded.read())).convert("RGB")
        result = demo_predict(image)
        return jsonify(result)
    except Exception as exc:
        return jsonify({"error": f"Unable to process image: {exc}"}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
