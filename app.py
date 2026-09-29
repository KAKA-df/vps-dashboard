from flask import Flask
from monitor import get_uptime_seconds

app = Flask(__name__)

@app.route("/")
def dashboard():
    uptime_seconds = get_uptime_seconds()
    return f"Uptime: {uptime_seconds}s\n"

@app.route("/health")
def ok():
    return "OK\n"

