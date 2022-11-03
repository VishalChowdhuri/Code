import time
import board
import touchio
import digitalio as dio
import neopixel
import random


blue = (0, 0, 255)
red = (255, 0 , 0)
yellow = (255, 255, 0)
black = (0, 0, 0)
green = (0, 255, 0)


num = 0
np = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5, auto_write=False)


over = True
gencolors = []


abutton = dio.DigitalInOut(board.BUTTON_A)
abutton.direction = dio.Direction.INPUT
abutton.pull = dio.Pull.DOWN
pad1 = board.A5
t1 = touchio.TouchIn(pad1)
pad2 = board.A6
t2 = touchio.TouchIn(pad2)
pad3 = board.A1
t3 = touchio.TouchIn(pad3)
pad4 = board.A2
t4 = touchio.TouchIn(pad4)
led = dio.DigitalInOut(board.LED)
led.direction = dio.Direction.OUTPUT


‘’’
Function: fgreen
Description: This function flashes the color green
Parameters: None
Return: None
‘’’
def fgreen():
    np.fill(green)
    np.show()
    time.sleep(0.1)
    np.fill(black)
    np.show()


‘’’
Function: fred
Description: This function flashes the color red
Parameters: None
Return: None
‘’’
def fred():
    np.fill(red)
    np.show()
    time.sleep(0.1)
    np.fill(black)
    np.show()


‘’’
Function: blink
Description: This function blinks 2 certain neopixels a certain color.
Parameters: Color, num, num1, color is the color that will set the 2 neopixels, num and num1 are the two neopixels.
Return: None
‘’’
def blink(num, num1, rgb):
    np[num] = rgb
    np[num1] = rgb


‘’’
Function: show
Description: This function will take in a number between 1-4 and show a certain color. For instance 1 will show red, 2 will show green, 3 will show blue, and 4 will show yellow.
Parameters: numcolor, this is the number that will be taken in and compared.
Return: None
‘’’
def show(numcolor):
    if numcolor == 1:
        blink(0,1,red)
        np.show()
        time.sleep(.5)
        blink(0,1,black)
        np.show()
    elif numcolor == 2:
        blink(3,4,green)
        np.show()
        time.sleep(.5)
        blink(3,4,black)
        np.show()
    elif numcolor == 3:
        blink(5,6,blue)
        np.show()
        time.sleep(.5)
        blink(5,6,black)
        np.show()
    elif numcolor == 4:
        blink(8,9,yellow)
        np.show()
        time.sleep(.5)
        blink(8,9,black)
        np.show()


‘’’
Function: nextround
Description: This function generates a random number between 1 and 4 and append it into the num list. Then it will show the sequence of colors using the function show. Then it will go through and verify if what is touched on the board correlates to what is on the list, if it is correct, it will flash green and move on to the next round or it will flash red and end.
Parameters: None
Return: None
‘’’
def nextround():
    num = random.randint(1,4)
    gencolors.append(num)
    for i in range(len(gencolors)):
        show(gencolors[i])
        time.sleep(1)
    for i in range(len(gencolors)):
        global over
        while (t1.value or t2.value or t3.value or t4.value) == False:
            pass
        if (t1.value and gencolors[i] == 1):
            show(gencolors[i])
        elif (t2.value and gencolors[i] == 2):
            show(gencolors[i])
        elif (t3.value and gencolors[i] == 3):
            show(gencolors[i])
        elif (t4.value  and gencolors[i] == 4):
            show(gencolors[i])
        else:
            over = True
    time.sleep(.1)


while True:
    if abutton.value == True:
        over = False
    if over == False:
        nextround()
        if over!= True:
            fgreen()
        else:
            fred()
        time.sleep(1)
    if over == True:
        gencolors = []
