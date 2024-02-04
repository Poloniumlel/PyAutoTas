# PyPcTAS (Python Task Automation Script)
PyTAS is a simple yet powerful Python script for automating repetitive tasks through keyboard and mouse inputs. Whether you're looking to streamline your workflow, perform repetitive actions in games ( **or make speedruns!!!** ), or automate sequences of interactions, PyTAS has got you covered.

## Features:
**Save and Load Mouse Location:** Store and retrieve the current mouse position effortlessly.  
**Wait for Frames:** Introduce delays by waiting for a specific number of frames (default frame rate is 60 fps, customizable in the code).  
**Execute Multiple Inputs in a Single Frame:** Execute a sequence of inputs line by line with precision timing.  
**Mouse Movements:** Move the mouse by a specified number of pixels, providing precise control.  
**Keyboard Input:** Press and release keys, including customizable key holding functionality.

## How It Works:
Simply create a text file with the desired sequence of inputs. Upon running the script and pressing the designated key (default is 'Insert'), PyTAS reads the file and executes the inputs sequentially. Each line corresponds to one frame, maintaining accuracy in execution.
## Usage:
- Create a text file in the same directory as the PyTAS script.  
 - Fill the text file with your desired input sequence (e.g., "save mouse,50,120 w s a d left load").  
- Run the script in the command line, specifying the text file as an argument (e.g., python PyTAS.py sequence.txt).  
- Press 'Insert' to initiate the sequence execution.
## Avalaiable Commands:
- **wait** - wait a specific amount of frames ( by default 1/60th of a second) example: wait120 ( waits 120 frames)
- **mouse** - moves mouse relative to current position , example: mouse,100,100
- **left** - left clicks
- **right** - right clicks
- **hold** - holds a specific key example: hold,z,120 ( holds z for 120 frames , or 2 sec for a selected framerate of 60 sec)
- **save** - saves current mouse position. doing this twice overides the old saved position
- **load** - loads the last saved mouse position (**WARNING** - Might not work in a lot of 3d games due to its implementation! ! !)
## Dependencies:
- **keyboard**
- **pyautogui**
- **pydirectinput**
## Installing Dependencies:
Open the command line and run:

```pip install keyboard pyautogui pydirectinput ```
