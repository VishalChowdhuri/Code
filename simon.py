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


pressed = False
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


'''
Function: flash_green
Description: This function flashes the color green
Parameters: None
Return: None
'''
def flash_green():
    np.fill(green)
    np.show()
    time.sleep(0.1)
    np.fill(black)
    np.show()


'''
Function: flash_red
Description: This function flashes the color red
Parameters: None
Return: None
'''
def flash_red():
    np.fill(red)
    np.show()
    time.sleep(0.1)
    np.fill(black)
    np.show()


'''
Function: blink
Description: This function blinks 2 certain neopixels a certain color.
Parameters: Color, num, num1, color is the color that will set the 2 neopixels, num and num1 are the two neopixels.
Return: None
'''
def blink(num, num1, rgb):
    np[num] = rgb
    np[num1] = rgb
    np.show()
    time.sleep(.5)
    np[num] = black
    np[num1] = black
    np.show()


'''
Function: show
Description: This function will take in a number between 1-4 and show a certain color. For instance 1 will show red, 2 will show green, 3 will show blue, and 4 will show yellow.
Parameters: numcolor, this is the number that will be taken in and compared.
Return: None
'''
def show(numcolor):
    if numcolor == 1:
        blink(0,1,red)
    elif numcolor == 2:
        blink(3,4,green)
    elif numcolor == 3:
        blink(5,6,blue)
    elif numcolor == 4:
        blink(8,9,yellow)


'''
Function: show_sequence
Description: This function will generate a random number between 1 and 4 and append that number to a list called gencolors. It will then go through the list 
and use the show function to show the colors.
Parameters: None
Return: None
'''
def show_sequence():
    num = random.randint(1,4)
    gencolors.append(num)
    for i in range(len(gencolors)):
        show(gencolors[i])
        time.sleep(.5)


'''
Function: next_round
Description: This function generates a random number between 1 and 4 and append it into the num list. Then it will show the sequence of colors using the function show. Then it will go through and verify if what is touched on the board correlates to what is on the list, if it is correct, it will flash green and move on to the next round or it will flash red and end.
Parameters: None
Return: None
'''
def next_round():
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
        elif (t4.value and gencolors[i] == 4):
            show(gencolors[i])
        else:
            over = True
    time.sleep(.1)


'''
Function: check_abutton
Description: This function will check if the abutton has been pressed
Parameters: None
Return: pressed and over values
'''
def check_abutton():
    global pressed
    global over
    if abutton.value == True and pressed == False:
        pressed = True
        over = False
        return pressed
        return over
    
#Displays the loop of the game
while True:
    check_abutton()
    if over == False:
        show_sequence()
        next_round()
        if over == False:
            flash_green()
        else:
            flash_red()
            pressed = False
            gencolors = []
        time.sleep(.5)
