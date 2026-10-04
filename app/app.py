from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "1.0.0")
ENVIRONMENT = os.getenv("ENVIRONMENT", "production")

@app.route("/")
def home():
    return render_template("index.html", version=VERSION, environment=ENVIRONMENT)

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "version": VERSION,
        "environment": ENVIRONMENT
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
