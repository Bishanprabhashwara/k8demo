from flask import Flask

app = Flask(__name__)
#test
@app.route("/")
def home():
    return "🚀 Hello from Flask on AKS with Docker & CI/CD!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
