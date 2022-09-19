import board

import neopixel

import time
import random

BRIGHTNESS = 1

rgb = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=BRIGHTNESS, auto_write=False)

nump = 10
'''
This code's name is sparkle, what it does is that it takes in 2 colors and a delay if needed, one
for the background color, the other for the sparkle. This one returns 4 random lights at the same
time.
'''
def sparkle(color1, color2, delay = .1):
    color = color1
    for i in range(nump):
        rgb[i] = color
    pix = random.randint(0, 9)
    pix2 = random.randint(0, 9)
    pix3 = random.randint(0, 9)
    rgb[pix] = color2
    pix4 = random.randint(0, 9)
    rgb[pix4] = color2
    rgb[pix2] = color2
    rgb[pix3] = color2

    rgb.show()
    time.sleep(delay)

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
    for i in range(30):

        sparkle((201,68,1), (30,10,1), 0.05)
