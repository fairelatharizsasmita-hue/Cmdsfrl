import platform
import sys
import os

def system_check():
    print("=== FRL SYSTEM CHECK ===")
    print("Platform:", platform.system())
    print("OS:", platform.release())
    print("Python:", sys.version.split()[0])
    print("Architecture:", platform.machine())
    print("Working Directory:", os.getcwd())

