from flask import Flask, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)

@app.route("/sync", methods=["POST"])
def receive_data():
    data = request.get_json()
    email = data.get("email", "unknown")
    videos = data.get("videos", [])

    # Створюємо окрему папку для зберігання
    os.makedirs("data", exist_ok=True)

    # Зберігаємо у файл з датою
    filename = f"data/{email}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(videos, f, ensure_ascii=False, indent=2)

    return jsonify({"status": "ok", "message": f"{len(videos)} videos received"})

if __name__ == "__main__":
    app.run(debug=True)
