<<<<<<< HEAD
from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter("hello_requests_total", "Total hello requests")

@app.route("/hello")
def hello():
    REQUEST_COUNT.inc()
    return jsonify({"message": "Hello DevOps with Jenkins & K8s!"})

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

=======
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask CI/CD with Jenkins + Ansible + K8s!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
>>>>>>> c5b1e3239a975390b4d4bdd3bccfb3ef13d81772
