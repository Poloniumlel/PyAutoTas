# Simple python implementation of what your usual tas app would let you do
## features:
keyboard and mouse inputs
saving and loading mouse location
waiting specific amount of frames ( by default the frame rate is 60 fps , can be changed in the code )
executing multiple inputs in a single frame
reading from a text file to get input sequence
## how it works:
The code lets you input a specific string of inputs into a text file. Then upon clicking insert ( changeable in the code ), it reads that file , and executes the inputs line by line. between each line theres a single frame ( by default 1/60th of a second , for 60 fps. can be set to different amounts but can stop being accurate on uncapped fps games )
if it finds a wait message , it waits for the specific amount of frames ( for example wait50 will wait 50 frames , or 5/6th of a second )
for a left or right message , it clicks the respective mouse button
save - saves the current mouse location. if one is already saved , overrides it.
load - loads the saved mouse location.
mouse - moves the mouse by specific amount of pixels ( example: mouse,50,50 moves the mouse 50 pixels up and 50 pixels right )
## How to use
Create a text file in the same directory as the code file.
fill it with the sequence you want
example "
save
mouse,50,120
w s
a d
left
load
"
run the program in the command line in the directory of the app with the text file as the argument ( replace sequence.txt with the name of your file ( python PyAutoTas.py sequence.txt )
click insert
it should now do the sequence you provided it with
## Dependencies:
time
keyboard
pyautogui
sys
### Installing dependencies:
open command line
run pip install {dependency name} ex: pip install pyautogui
