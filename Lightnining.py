import board
import time
import neopixel
import random

num_pixels = 10
np = neopixel.NeoPixel(board.NEOPIXEL, num_pixels, brightness=1.0, auto_write=False)

def constrain(low, high, value):
    if value < low:
        return low
    if value > high:
        return high
    return value

np.fill((255, 127, 0))
np.show()

'''
Function: Fire
Description: Creates a flame effect on a strip of neopixels
Parameters: background: base color for flame, foreground: color used to flash / highlight
return value: none
'''
def fire(background, foreground, delay = 0.1):
    for j in range(20):
        intensity = random.random() * 0.7 + 0.3
        i_background = [int(i * intensity) for i in background]
        np.fill(i_background)
        for i in range(random.randint(2, int(num_pixels/5))):
            intensity = random.random() * 0.7 + 0.3
            i_foreground = [int(i * intensity) for i in foreground]
            np[random.randint(0, num_pixels-1)] = i_foreground
        np.show()
        time.sleep(delay)

while True:
        fire((26,14,32), (5,5,5))
        if random.randint(0,5) > 2:
            delay = random.random()/25
            fire((255,255,255), (100,100,100), delay)
