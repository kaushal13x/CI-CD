from flask import Flask 

app = Flask(__name__)

@app.route("/")

def home():
    return "Hello From Deployed Via Jenkins & Docker Kaushal Kumar"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)

