import board
import neopixel
import time
import random
import digitalio as dio 
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A3, echo_pin=board.A4)
num_pixels = 30
rgb = neopixel.NeoPixel(board.A7, num_pixels, brightness=0.1, auto_write=False)
i = 0
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
while True:
    if(sonar.distance < 10.0 and i < 30):
        rgb[i] = blue
        i+=1
        rgb.show()
        time.sleep(.1)
    elif(sonar.distance > 10.0 and i <= 30 and i > 0):
        i -=1
        rgb[i] = [0,0,0]
        rgb.show()
        time.sleep(.1)
    else:
        if i > 0:
            i-=1
        else:
            i+=1
        pass
        
        
