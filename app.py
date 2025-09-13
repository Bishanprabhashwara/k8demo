from flask import Flask
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
#test
@app.route("/")
def home():
    env_var1 = os.environ.get('ENV_VAR_1', 'DEFAULT_VAR_1')
    env_var2 = os.environ.get('ENV_VAR_2', 'DEFAULT_VAR_2')
    return f"🚀 Hello from Flask on AKS with Docker & CI/CD! Environment Vars: {env_var1}, {env_var2}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
