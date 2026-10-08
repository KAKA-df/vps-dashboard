import shutil, psutil


def get_uptime_seconds():
    with open("/proc/uptime", "r") as file:
        uptime = file.read().split()
        uptime_seconds = int(float(uptime[0]))
    return uptime_seconds


def get_total_memory_kb():
    with open("/proc/meminfo", "r") as file:
        meminfo = file.readline().split()
    return int(meminfo[1])


def get_available_memory_kb():
    with open("/proc/meminfo", "r") as file:
        for i, line in enumerate(file):
            if i == 2:
                return int(line.split()[1])


def get_memory_usage_percent():
    total_memory_kb = get_total_memory_kb()
    available_memory_kb = get_available_memory_kb()
    used_memory_kb = total_memory_kb - available_memory_kb
    used_memory_percent = used_memory_kb / total_memory_kb * 100
    return used_memory_percent


def get_root_disk_usage():
    return shutil.disk_usage("/")


def get_cpu_usage_percent():
    return psutil.cpu_percent(interval=1)


if __name__ == "__main__":
    uptime_seconds = get_uptime_seconds()
    minutes = uptime_seconds // 60
    seconds = uptime_seconds % 60
    print("Uptime:", minutes, "min", seconds, "s")

    used_memory_percent = get_memory_usage_percent()
    print("RAM usage:", round(used_memory_percent, 1), "%")

    disk_usage = get_root_disk_usage()
    total_gib = disk_usage.total / 1024 ** 3
    used_gib = disk_usage.used / 1024 ** 3
    free_gib = disk_usage.free / 1024 ** 3

    cpu_usage = get_cpu_usage_percent()    
    print("Total disk:", round(total_gib, 1), "GiB")
    print("Used disk:", round(used_gib, 1), "GiB")
    print("Free disk:", round(free_gib, 1), "GiB")
    print("CPU usage (1-second sample):", round(cpu_usage, 1), "%")
