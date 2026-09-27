with open("/proc/uptime", "r") as file:
    uptime = file.read().split()
    uptime_seconds = int(float(uptime[0]))
    minutes = uptime_seconds // 60
    seconds = uptime_seconds % 60
    print("Uptime:", minutes, "min", seconds, "s")

