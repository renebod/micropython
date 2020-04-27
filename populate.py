import machine, neopixel
np = neopixel.NeoPixel(machine.Pin(2), 24)
from random import randint
import time

black = (0, 0, 0)
blue = (0, 0, 16)

b = 16 # brightness
n = np.n

def change_led(np):
    led = randint(0, (n - 1))
    speed = randint(15, 90)
    if np[led] == blue:
        for i in range(b + 1):
            i = b - i
            np[led] = (0, 0, i)
            np.write()
            time.sleep_ms(speed)
    else:
        for i in range(b + 1):
            np[led] = (0, 0, i)
            np.write()
            time.sleep_ms(speed)
    print("Led: " + str(led) + " is changed")
    time.sleep_ms(randint(60, 720))

while True:
    change_led(np)
