import vgamepad as vg
import pygetwindow as gw
import pyautogui
from PIL import Image
import pytesseract
import math
import time


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
controller = vg.VX360Gamepad()

print("Starting virtual controller example...")
print("Press Ctrl+C to stop.")


def press_A():
    controller.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    controller.update()
    time.sleep(0.5)

    controller.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    controller.update()
    time.sleep(0.5)

def move_left_stick(x_value, y_value):
    controller.left_joystick_float(x_value_float=x_value, y_value_float=y_value)
    controller.update()
    time.sleep(0.5)

def setup_controller():
    controller.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    controller.update()
    time.sleep(1)
    print("Pressing A button")
    controller.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    controller.update()
    print("Releasing A button")
    time.sleep(1)

    controller.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    controller.update()
    time.sleep(1)
    print("Pressing B button")
    controller.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    controller.update()
    print("Releasing B button")


    controller.reset()
    controller.update()
    time.sleep(1)

def move_cursor(current_pos, target_pos, speed = 1, step_time = 0.05):
    x0, y0 = current_pos
    x1, y1 = target_pos
    dx = x1 - x0
    dy = y1 - y0
    distance = math.hypot(dx, dy) / 10
    print(f"Distance is {distance}")
    if distance == 0:
        return
    
    direction_x = dx / distance
    direction_y = dy / distance
    print(f"Direction is ({direction_x}, {direction_y})")

    steps = int(distance / speed)
    for _ in range(steps):
        controller.left_joystick_float(direction_x, -direction_y)
        controller.update()
        time.sleep(step_time)
    
    controller.reset()
    controller.update()

def select_rob():
    controller.left_joystick_float(0, 1)
    controller.update()
    time.sleep(.43)

    controller.left_joystick_float(-1, 0)
    controller.update()
    time.sleep(.4)

    controller.reset()
    controller.update()
    time.sleep(0.6)

    for _ in range(5):
        controller.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
        controller.update()
        time.sleep(0.1)
        controller.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
        controller.update()
        time.sleep(0.05)

    controller.reset()
    controller.update()

    press_A()



try:
    input("Press Enter to start the controller setup...")

    # setup_controller()
    press_A()

    while True:
        if input("Press Enter to select ROB...") == "":
            select_rob()

        

except KeyboardInterrupt:
    print("Stopping virtual controller example...")