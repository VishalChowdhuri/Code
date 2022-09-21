import board

import neopixel

import time
import random

BRIGHTNESS = .3

rgb = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=BRIGHTNESS, auto_write=False)

nump = 10
'''
This code's name is sparkle, what it does is that it takes in 2 colors and a delay if needed, one 
for the background color, the other for the sparkle. This one returns 4 random lights at the same 
time.
'''
def sparkle(color, color1, loop = 10, delay=0.1):
  for i in range(loop):
    rgb.fill(color)
    for q in range(rgb.n / 4):
      rgb[random.randint(0, rgb.n-1)] = color1
    rgb.show()
    time.sleep(delay)
'''
This code’s name is fade out, what it does is fade out from the color given by individually minusing every  
'''
def fade_out(color, sec = 0.001):
    mx = max(color[0], max(color[1], color[2]))
    r_inc = color[0]/mx
    g_inc = color[1]/mx
    b_inc = color[2]/mx
    r, g, b = color
    while r >= 0 and g >= 0 and b >= 0:
        r -= r_inc
        g -= g_inc
        b -= b_inc
        rgb.fill((int(r), int(g), int(b)))
        rgb.show()
        time.sleep(sec)

def fade_in(color, sec = 0.001):
    r, g, b = color
    r1 = r
    g1 = g
    b1 = b
    mx = max(color[0], max(color[1], color[2]))
    r_inc = color[0]/mx
    g_inc = color[1]/mx
    b_inc = color[2]/mx
    r = 0
    b = 0
    g = 0
    while r < r1  and g < g1 and b < b1:
        r += r_inc
        g += g_inc
        b += b_inc
        rgb.fill((int(r), int(g), int(b)))
        rgb.show()
        time.sleep(sec)
def chase(color1, color2, loop=20, count=3, delay=0.1):
    result = 0
    for outer in range(count * loop):
        rgb.fill(color1)
        for i in range(nump):
            if i % count == result:
                rgb[i] = color2
        rgb.show
        time.sleep(delay)
        result += 1
        result %= count
        rgb.show()




while True:
# These set the colors used in this program as variables
#  Sets the variable, blue   
    blue = [255,1,1]
# Sets the variable, red    
    red = [1, 1, 255]
# Sets the variable, light blue    
    lightb = [20,255,240]
# Sets the variable, pink
    pink = [235,0,15]
# This will fade in the color blue
    fade_in(blue)
# This will make the sparkle effect 30 times 
    for i in range(30):
        sparkle((blue), (red), 0.01)

    chase((red), (blue), loop = 10, count = 2, delay=0.1)
    chase((red), (blue), loop = 10, count = 2, delay=0.05)
    chase((0, 0 , 0), (blue), loop = 20, count = 3, delay=0.01)
    fade_out((blue))
    fade_in(lightb)
    chase((lightb), (pink), loop = 10, count = 4, delay=0.05)
    chase((lightb), (pink), loop = 10, delay=0.05)
    chase((lightb), (pink), loop = 10, count = 2, delay=0.05)
    chase((lightb), (pink), loop = 10, count = 2, delay=0.05)
    chase((0,0,0), (pink), loop = 20, count = 3, delay=0.01)
    fade_out((pink))
    
