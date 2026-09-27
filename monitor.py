with open("/proc/uptime", "r") as file:
    uptime = file.read().split()
    print("Uptime in seconds:", float(uptime[0]))

