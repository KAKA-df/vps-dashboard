from flask import Flask
from flask import render_template
from monitor import get_uptime_seconds, get_memory_usage_percent, get_root_disk_usage, get_cpu_usage_percent, format_uptime

app = Flask(__name__)

@app.route("/")
def dashboard():
    uptime_seconds = get_uptime_seconds()
    uptime_text = format_uptime(uptime_seconds)
    used_memory_percent = get_memory_usage_percent()
    disk_usage = get_root_disk_usage()
    total_disk_gib = disk_usage.total / 1024 ** 3
    used_disk_gib = disk_usage.used / 1024 ** 3

    cpu_usage_percent = get_cpu_usage_percent()

    return render_template('dashboard.html', uptime_text=uptime_text, used_memory_percent=round(used_memory_percent, 1), used_disk_gib=round(used_disk_gib, 1), total_disk_gib=round(total_disk_gib, 1), cpu_usage_percent=round(cpu_usage_percent, 1))

