from flask import Flask
from monitor import get_uptime_seconds, get_memory_usage_percent

app = Flask(__name__)

@app.route("/")
def dashboard():
    uptime_seconds = get_uptime_seconds()
    used_memory_percent = get_memory_usage_percent()
    return f"<h1>Server dashboard</h1><p>Uptime: {uptime_seconds}s.</p><p>RAM usage: {round(used_memory_percent, 1)}%</p>"

@app.route("/health")
def ok():
    return "OK\n"

