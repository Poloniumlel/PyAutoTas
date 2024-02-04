import sys
import time
import keyboard
import pydirectinput
import pyautogui
from threading import Thread

# Constants for short names in the sequence file
SAVE_MOUSE = "save"
LOAD_MOUSE = "load"
LEFT_CLICK = "left"
RIGHT_CLICK = "right"
MOVE_MOUSE = "mouse"
HOLD_KEY = "hold"

# A single variable to store the current saved mouse position
current_saved_mouse_position = None

def wait_for_insert_key():
    print("Press 'Insert' key to start the input execution.")
    while True:
        if keyboard.is_pressed("insert"):
            break
        time.sleep(0.1)

def hold_key(key, frames):
    keyboard.press(key)  # Key down
    time.sleep(frames / 60)  # Wait for the specified number of frames
    keyboard.release(key)  # Key up

def play_sequence(frames):
    threads = []
    for frame in frames:
        keys = frame.strip().split()

        for key in keys:
            if key.startswith('wait'):
                wait_frames = int(key[4:])
                time.sleep(wait_frames / 60)
            elif key == LEFT_CLICK:
                pydirectinput.click(button='left')
            elif key == RIGHT_CLICK:
                pydirectinput.click(button='right')
            elif key == SAVE_MOUSE:
                global current_saved_mouse_position
                current_saved_mouse_position = pydirectinput.position()
            elif key == LOAD_MOUSE:
                if current_saved_mouse_position:
                    x, y = current_saved_mouse_position
                    pydirectinput.moveTo(x, y)
            elif key.startswith(MOVE_MOUSE):
                _, dx, dy = key.split(',')
                x, y = pydirectinput.position()
                pydirectinput.moveRel(int(dx), int(dy), duration=0.3, relative=True)
            elif key.startswith(HOLD_KEY):
                _, hold_key_value, hold_frames = key.split(',')
                hold_frames = int(hold_frames)
                thread = Thread(target=hold_key, args=(hold_key_value, hold_frames))
                thread.start()
                threads.append(thread)
            else:
                keyboard.press(key)

        time.sleep(1 / 60)

        for key in keys:
            if not any(key.startswith(prefix) for prefix in ['wait', SAVE_MOUSE, LOAD_MOUSE, LEFT_CLICK, RIGHT_CLICK, MOVE_MOUSE, HOLD_KEY]):
                keyboard.release(key)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            print("Usage: python script.py <file_path>")
            sys.exit(1)

        file_path = sys.argv[1]

        with open(file_path, 'r') as file:
            input_sequence = file.readlines()

        wait_for_insert_key()

        for frame in input_sequence:
            keys = frame.strip().split()
            play_sequence(keys)

    except Exception as e:
        print(f"Error: {e}")
