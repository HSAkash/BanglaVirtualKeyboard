from utils.cameraUtils import (
    list_cameras,
)
from virtualKeyboard.virtual_Keyboard import vk



if __name__ == "__main__":


    # Get the list of camera devices connected to the system
    cam_devices = list_cameras()
    cam_index = int(input("Enter the camera index: "))

    # Horizontal and vertical flip
    h_flip = input("Do you want to flip the video horizontally? (y/n): ")
    v_flip = input("Do you want to flip the video vertically? (y/n): ")
    h_flip = h_flip.lower() == "y"
    v_flip = v_flip.lower() == "y"

    # Start the virtual keyboard
    vk(cam_index, h_flip, v_flip)


