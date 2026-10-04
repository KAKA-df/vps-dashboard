from flask import Flask
from flask import render_template
from monitor import get_uptime_seconds, get_memory_usage_percent

app = Flask(__name__)

@app.route("/")
def dashboard():
    uptime_seconds = get_uptime_seconds()
    used_memory_percent = get_memory_usage_percent()
    return render_template('dashboard.html', uptime_seconds=uptime_seconds, used_memory_percent=round(used_memory_percent, 1))

@app.route("/health")
def ok():
    return "OK\n"

