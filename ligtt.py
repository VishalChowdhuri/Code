# Write your code here :-)
import board
import digitalio as dio
import time
import touchio
import random
import neopixel

pad1= board.A1
pad2= board.A2
pad3= board.A3
pad4= board.A4

t1= touchio.TouchIn(pad1)
t2= touchio.TouchIn(pad2)
t3= touchio.TouchIn(pad3)
t4= touchio.TouchIn(pad4)

num_pixels = 10
np = neopixel.NeoPixel(board.NEOPIXEL, num_pixels, brightness=1.0, auto_write=False)

def blink(num, num1, rgb):
    np[num] = color
    np[num1] = color

while True:
    if t1.value == True:
        rgb=[0,255,0]
        np.fill(rgb)
        np.show()
        time.sleep(0.05)
    else:
        rgb = [0,0,0]
        np.fill(rgb)
        np.show()
        time.sleep(0.05)

