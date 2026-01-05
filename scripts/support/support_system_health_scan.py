import psutil
import platform
import time
import os

try:
    import wmi
    w = wmi.WMI(namespace="root\\OpenHardwareMonitor")
except Exception:
    w = None

ISSUES = []

def check_cpu():
    cpu = psutil.cpu_percent(interval=3)
    if cpu > 85:
        ISSUES.append(
            f"🔥 High CPU usage ({cpu}%). Fix: identify runaway processes, disable startup apps, check for background builds or malware."
        )

def check_memory():
    mem = psutil.virtual_memory()
    if mem.percent > 80:
        ISSUES.append(
            f"🧠 High RAM usage ({mem.percent}%). Fix: close memory-hog apps, add RAM, or stop Chrome abuse."
        )

def check_disk():
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            if usage.percent > 85:
                ISSUES.append(
                    f"💾 Disk nearly full on {part.device} ({usage.percent}%). Fix: delete junk, move repos/media, expand disk."
                )
        except:
            pass

def check_uptime():
    uptime_hours = (time.time() - psutil.boot_time()) / 3600
    if uptime_hours > 240:
        ISSUES.append(
            f"⏱️ System uptime {int(uptime_hours)}h. Fix: reboot weekly to prevent memory leaks and driver weirdness."
        )

def check_processes():
    heavy = []
    for p in psutil.process_iter(['name', 'cpu_percent', 'memory_percent']):
        try:
            if p.info['cpu_percent'] > 50 or p.info['memory_percent'] > 20:
                heavy.append(p.info)
        except:
            pass

    if heavy:
        ISSUES.append(
            "⚠️ Heavy processes detected. Fix: inspect Task Manager → kill or fix offenders."
        )

def check_temp():
    if not w:
        return
    temps = []
    for sensor in w.Sensor():
        if sensor.SensorType == 'Temperature':
            temps.append(sensor.Value)

    if temps and max(temps) > 85:
        ISSUES.append(
            f"🌡️ CPU temperature high ({max(temps)}°C). Fix: clean fans, replace thermal paste, improve airflow."
        )

def main():
    print("=" * 60)
    print("🩺 SYSTEM HEALTH SCAN")
    print("=" * 60)
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"CPU Cores: {psutil.cpu_count(logical=True)}")
    print(f"RAM: {round(psutil.virtual_memory().total / (1024**3),1)} GB")
    print("-" * 60)

    check_cpu()
    check_memory()
    check_disk()
    check_uptime()
    check_processes()
    check_temp()

    if not ISSUES:
        print("✅ System looks healthy. No action needed.")
    else:
        print("🚨 ISSUES FOUND:")
        for issue in ISSUES:
            print(f"- {issue}")

    print("=" * 60)

if __name__ == "__main__":
    main()
