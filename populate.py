import machine, neopixel
np = neopixel.NeoPixel(machine.Pin(2), 24)
from random import randint
import time

black = (0, 0, 0)
blue = (0, 0, 16)

def change_led(np):
    led = randint(0, (np.n - 1))
    speed = randint(30, 60)
    if np[led] == blue:
        for i in range(0, 17):
            i = 16 - i
            np[led] = (0, 0, i)
            np.write()
            time.sleep_ms(speed)
    else:
        for i in range(0, 17):
            np[led] = (0, 0, i)
            np.write()
            time.sleep_ms(speed)
    print("Led: " + str(led) + " is changed)
    time.sleep_ms(randint(60, 720))

while True:
    change_led(np)
