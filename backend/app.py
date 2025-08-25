from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from process_video import process_video

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "backend/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"})


@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "❌ No file uploaded"}), 400

    file = request.files["file"]
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # ประมวลผลวิดีโอ
    result = process_video(filepath)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
