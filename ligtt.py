# Write your code here :-)
import board
import digitalio as dio
import time
import touchio
import random
import neopixel

pad1= board.A1
pad2= board.A2
pad3= board.A5
pad4= board.A6

t1= touchio.TouchIn(pad1)
t2= touchio.TouchIn(pad2)
t3= touchio.TouchIn(pad3)
t4= touchio.TouchIn(pad4)

num_pixels = 10
np = neopixel.NeoPixel(board.NEOPIXEL, num_pixels, brightness=1.0, auto_write=False)
gen = []
user = []
def blink(num, num1, rgb):
    np[num] = rgb
    np[num1] = rgb

while True:
    if t3.value == True:
        rgb=[0,255,0]
        blink(0,1,rgb)
        np.show()
        time.sleep(0.05)
        user.append(3)
        print(user)
        time.sleep(1)
    else:
        rgb = [0,0,0]
        blink(0,1,rgb)
        np.show()
        time.sleep(0.05)
    if t1.value == True:
        rgb=[255,255,0]
        blink(5,6,rgb)
        np.show()
        time.sleep(0.05)
        user.append(1)
        print(user)
        time.sleep(1)
    else:
        rgb = [0,0,0]
        blink(5,6,rgb)
        np.show()
        time.sleep(0.05)
    if t2.value == True:
        rgb=[255,0,0]
        blink(8,9,rgb)
        np.show()
        time.sleep(0.05)
        user.append(2)
        print(user)
        time.sleep(1)
    else:
        rgb = [0,0,0]
        blink(8,9,rgb)
        np.show()
        time.sleep(0.05)
    if t4.value == True:
        rgb=[0,0,255]
        blink(3,4,rgb)
        np.show()
        user.append(4)
        print(user)
        time.sleep(.5)
    else:
        rgb = [0,0,0]
        blink(3,4,rgb)
        np.show()
        time.sleep(0.05)

