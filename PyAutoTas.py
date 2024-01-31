import sys
import time
import keyboard
import pyautogui

# Constants for short names in the sequence file
SAVE_MOUSE = "save"
LOAD_MOUSE = "load"
LEFT_CLICK = "left"
RIGHT_CLICK = "right"
MOVE_MOUSE = "mouse"

# A single variable to store the current saved mouse position
current_saved_mouse_position = None

def wait_for_insert_key():
    print("Press 'Insert' key to start the input execution.")
    while True:
        if keyboard.is_pressed("insert"):
            break
        time.sleep(0.1)

def play_sequence(frames):
    for frame in frames:
        keys = frame.strip().split()

        for key in keys:
            if key.startswith('wait'):
                wait_frames = int(key[4:])
                time.sleep(wait_frames / 60)  # Introducing frame-perfect wait
            elif key == LEFT_CLICK:
                pyautogui.click(button='left')
            elif key == RIGHT_CLICK:
                pyautogui.click(button='right')
            elif key == SAVE_MOUSE:
                global current_saved_mouse_position
                current_saved_mouse_position = pyautogui.position()
            elif key == LOAD_MOUSE:
                if current_saved_mouse_position:
                    pyautogui.moveTo(current_saved_mouse_position)
            elif key.startswith(MOVE_MOUSE):
                _, dx, dy = key.split(',')
                pyautogui.move(int(dx), int(dy))
            else:
                keyboard.press(key)

        for key in keys:
            if not any(key.startswith(prefix) for prefix in ['wait', SAVE_MOUSE, LOAD_MOUSE, LEFT_CLICK, RIGHT_CLICK, MOVE_MOUSE]):
                keyboard.release(key)

        time.sleep(1 / 60)  # Introducing frame-based wait between each line

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            print("Usage: python script.py <file_path>")
            sys.exit(1)

        file_path = sys.argv[1]

        with open(file_path, 'r') as file:
            input_sequence = file.readlines()

        wait_for_insert_key()  # Wait for the 'Insert' key to be pressed before starting the input execution

        for frame in input_sequence:
            keys = frame.strip().split()
            play_sequence(keys)

    except Exception as e:
        print(f"Error: {e}")
