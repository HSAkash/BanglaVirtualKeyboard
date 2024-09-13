"""
Get the list of camera devices connected to the system
"""
import platform
import sys

# Linux-specific import
try:
    import pyudev
except ImportError:
    pyudev = None

# Windows-specific import
try:
    import win32com.client
except ImportError:
    win32com = None

# Function for Linux
def list_cameras_linux():
    if pyudev is None:
        print("pyudev is not installed. Please install it using `pip install pyudev`.")
        return
    context = pyudev.Context()
    for i, device in enumerate(context.list_devices(subsystem='video4linux')):
        print(f"{i} :- Device Node: {device.device_node}, Model: {device.get('ID_MODEL')}")

# Function for Windows
def list_cameras_windows():
    if win32com is None:
        print("pywin32 is not installed. Please install it using `pip install pywin32`.")
        return
    wmi = win32com.client.GetObject("winmgmts:")
    cameras = wmi.InstancesOf("Win32_PnPEntity")
    i = 0
    for camera in cameras:
        if "camera" in camera.Name.lower() or "imaging" in camera.Name.lower():
            print(f"{i:}:- Device Name: {camera.Name} Device ID: {camera.DeviceID}")

# Function for macOS
def list_cameras_macos():
    import subprocess
    result = subprocess.run(["system_profiler", "SPCameraDataType"], capture_output=True, text=True)
    print(result.stdout)

# Main function to detect OS and list cameras
def list_cameras():
    os_type = platform.system()

    if os_type == "Linux":
        list_cameras_linux()
    elif os_type == "Windows":
        list_cameras_windows()
    elif os_type == "Darwin":  # macOS
        list_cameras_macos()
    else:
        print(f"Unsupported OS: {os_type}")

