def get_uptime_seconds():
    with open("/proc/uptime", "r") as file:
        uptime = file.read().split()
        uptime_seconds = int(float(uptime[0]))
    return uptime_seconds


def get_total_memory_kb():
    with open("/proc/meminfo", "r") as file:
        meminfo = file.readline().split()
    return int(meminfo[1])


uptime_seconds = get_uptime_seconds()
minutes = uptime_seconds // 60
seconds = uptime_seconds % 60
print("Uptime:", minutes, "min", seconds, "s")

total_memory_kb = get_total_memory_kb()
print("Total RAM:", total_memory_kb, "kB")
