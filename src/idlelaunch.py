import ctypes
import time
import subprocess
import os
import sys

monitor_is_on = True
DEFAULT_IDLE_MINUTES = 10

def get_app_folder():
    return os.path.dirname(os.path.abspath(sys.argv[0]))

def get_idle_minutes():
    try:
        path = os.path.join(get_app_folder(), "idletime.txt")
        with open(path, "r") as f:
            minutes = int(f.read().strip())
            print(f"Idle timeout loaded: {minutes} minutes")
            return minutes * 60
    except Exception as e:
        print(f"Could not read idletime.txt, using default ({DEFAULT_IDLE_MINUTES} min). Error: {e}")
        return DEFAULT_IDLE_MINUTES * 60

def get_idle_duration():
    class LASTINPUTINFO(ctypes.Structure):
        _fields_ = [("cbSize", ctypes.c_uint), ("dwTime", ctypes.c_uint)]
    lii = LASTINPUTINFO()
    lii.cbSize = ctypes.sizeof(LASTINPUTINFO)
    ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lii))
    return (ctypes.windll.kernel32.GetTickCount() - lii.dwTime) / 1000.0

def run_shortcut(filename):
    path = os.path.join(get_app_folder(), filename)
    if os.path.exists(path):
        subprocess.Popen(['cmd', '/c', 'start', '', path], shell=True)

def main():
    global monitor_is_on
    idle_threshold = get_idle_minutes()
    print("Monitoring idle state. Press Ctrl+C to quit.")
    try:
        while True:
            idle = get_idle_duration()
            if idle >= idle_threshold and monitor_is_on:
                print("Idle threshold reached. Triggering OFF shortcut.")
                run_shortcut("openrgb-off.lnk")
                monitor_is_on = False
            elif idle < 1 and not monitor_is_on:
                print("User activity detected. Triggering ON shortcut.")
                run_shortcut("openrgb-on.lnk")
                monitor_is_on = True
            time.sleep(3)
    except KeyboardInterrupt:
        print("Stopped.")

if __name__ == "__main__":
    main()