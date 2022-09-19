import board
import time
import neopixel

num_pixels = 10
np = neopixel.NeoPixel(board.NEOPIXEL, num_pixels, brightness=.2, auto_write=False)

increase = True
rgb = [255, 0, 0]

while True:
    # red to yellow
    if increase and rgb[0] == 255 and rgb[1] < 255:
        rgb[1] += 15
    if increase and rgb == [255, 255, 0]:
        increase = not increase

    # yellow to green
    if not increase and rgb[1] == 255 and rgb[0] > 0:
        rgb[0] -= 15
    if not increase and rgb == [0, 255, 0]:
        increase = not increase

    #green to cyan
    if increase and rgb[1] == 255 and rgb[2] < 255:
        rgb[2] += 15
    if increase and rgb == [0, 255, 255]:
        increase = not increase

    # cyan to blue
    if not increase and rgb[2] == 255 and rgb[1] > 0:
        rgb[1] -= 15
    if not increase and rgb == [0, 0, 255]:
        increase = not increase

    # blue to magenta
    if increase and rgb[2] == 255 and rgb[0] < 255:
        rgb[0] += 15
    if increase and rgb == [255, 0, 255]:
        increase = not increase
    
    # magenta to red
    if not increase and rgb[0] == 255 and rgb[2] > 0:
        rgb[2] -= 15
    if not increase and rgb == [255, 0, 0]:
        increase = not increase
    np.fill(rgb)
    np.show()
    time.sleep(0.01)
