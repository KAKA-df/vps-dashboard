def get_uptime_seconds():
    with open("/proc/uptime", "r") as file:
        uptime = file.read().split()
        uptime_seconds = int(float(uptime[0]))
    return uptime_seconds


uptime_seconds = get_uptime_seconds()
minutes = uptime_seconds // 60
seconds = uptime_seconds % 60
print("Uptime:", minutes, "min", seconds, "s")

