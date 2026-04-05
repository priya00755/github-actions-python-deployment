from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Priya 🚀 Deployed via GitHub Actions!"

app.run(host="0.0.0.0", port=5000)
