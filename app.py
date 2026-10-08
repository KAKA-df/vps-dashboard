from flask import Flask
from flask import render_template
from monitor import get_uptime_seconds, get_memory_usage_percent, get_root_disk_usage

app = Flask(__name__)

@app.route("/")
def dashboard():
    uptime_seconds = get_uptime_seconds()
    used_memory_percent = get_memory_usage_percent()
    disk_usage = get_root_disk_usage()
    total_disk_gib = disk_usage.total / 1024 ** 3
    used_disk_gib = disk_usage.used / 1024 ** 3

    return render_template('dashboard.html', uptime_seconds=uptime_seconds, used_memory_percent=round(used_memory_percent, 1), used_disk_gib=round(used_disk_gib, 1), total_disk_gib=round(total_disk_gib, 1))

@app.route("/health")
def ok():
    return "OK\n"

