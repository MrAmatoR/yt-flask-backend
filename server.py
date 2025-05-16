from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import os, json

app = Flask(__name__)
CORS(app)  # ✅ Дозволяємо запити з інших джерел

@app.route("/sync", methods=["POST"])
def sync():
    data = request.get_json()
    email = data.get("email", "unknown")
    videos = data.get("videos", [])

    os.makedirs("data", exist_ok=True)
    filename = f"data/{email}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(videos, f, ensure_ascii=False, indent=2)

    return jsonify({"status": "ok", "message": f"{len(videos)} videos received"})
