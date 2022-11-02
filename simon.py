import time
import board
import touchio
import digitalio as dio
import neopixel
import random
#Creating variable names for colors that will be used throughout the program.
red = (255, 0 , 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
#Creating the list that will keep track of the colors displayed.
gencolors = []
num = 0
np = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5, auto_write=False)
#Creating variable to determine if the game is over or not.
over = True

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
#Both these defs will flash a certain color when called, fgreen will flash green and fred will flash red.
def fgreen():
    np.fill(green)
    np.show()
    time.sleep(0.1)
    np.fill(black)
    np.show()
def fred():
    np.fill(red)
    np.show()
    time.sleep(0.1)
    np.fill(black)
    np.show()
#This function will assign colors to two seperate lights.
def blink(num, num1, rgb):
    np[num] = rgb
    np[num1] = rgb
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
