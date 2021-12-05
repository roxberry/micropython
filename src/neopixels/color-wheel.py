from utime import sleep
from neopixel import Neopixel

NUMBER_PIXELS = 2
STATE_MACHINE = 0
NEOPIXEL_PIN = 18

strip = Neopixel(NUMBER_PIXELS, STATE_MACHINE, NEOPIXEL_PIN, "GRB")
strip.brightness(100)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(rc_index & 255)
        pixels.write()
        
counter = 0
while True:
    for i in range(0, NUMBER_PIXELS):
        # print(wheel(counter))
        strip.set_pixel(i, wheel(counter))
    strip.show()
    counter += 1
    counter = counter % 255
    sleep(.01)
