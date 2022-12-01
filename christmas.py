import board
import neopixel
import time
import random
import digitalio as dio

num_pixels = 30
rgb = neopixel.NeoPixel(board.A3, num_pixels, brightness=0.1, auto_write=False)

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
def stripes(space, color, colorsize, num_pixels):
    index = space
    once = False
    if space>0 and space <30:
        stripe = int(num_pixels / colorsize)
    else:
        stripe = int(num_pixels)
    for i in range(stripe):
        if space <= colorsize:
            if index > num_pixels-(space) and once:
                time.sleep(1)
                break
        else:
            if index > num_pixels-(colorsize) and once:
                time.sleep(1)
                break
        for j in range(colorsize):
            rgb[j+index]= color
            rgb.show()
            time.sleep(.1)
        index += (colorsize + space)
        once = True
while True:
    white = [255,255,255]
    fade_in(white)
    stripes(3,[255,0,0],3,30)
    fade_out(white)
    
