"""
Created by: Jayden Okafor
Created on: Mar 2026
This program turns all the pixels colour to red if the distance is below 10cm
and turns them green if distance is above 10cm
"""

from microbit import *
import neopixel

# variables
neopixelStrip = neopixel.NeoPixel(pin16, 4)
distanceToObject = None

# clear screen
display.clear()
display.show(Image.HAPPY)

# turn all 4 pixels off
neopixelStrip[0] = (0, 0, 0)
neopixelStrip[1] = (0, 0, 0)
neopixelStrip[2] = (0, 0, 0)
neopixelStrip[3] = (0, 0, 0)
neopixelStrip.show()


# library
class HCSR04:
    def __init__(self, tpin=pin1, epin=pin2, spin=pin13):
        self.trigger_pin = tpin
        self.echo_pin = epin
        self.sclk_pin = spin

        spi.init(
            baudrate=125000,
            sclk=self.sclk_pin,
            mosi=self.trigger_pin,
            miso=self.echo_pin,
        )

        self.length = 500
        self.resp = bytearray(self.length)

    def distance_mm(self):
        pre = 0
        post = 0
        k = -1
        length = self.length
        resp = self.resp

        for j in range(length):
            resp[j] = 0
        resp[0] = 0xFF

        spi.write_readinto(resp, resp)

        try:
            i, value = next((ind, v) for ind, v in enumerate(resp) if v)
        except StopIteration:
            i = -1
        if i > 0:
            pre = bin(value).count("1")
            try:
                k, value = next(
                    (ind, v)
                    for ind, v in enumerate(resp[i : length - 2])
                    if resp[i + ind + 1] == 0
                )
                post = bin(value).count("1") if k else 0
                k = k + i
            except StopIteration:
                i = -1
        dist = -1 if i < 0 else round(((pre + (k - i) * 8.0 + post) * 8 * 0.172) / 2)
        return dist


# assign the class library to the sonar variable
sonar = HCSR04()

while True:
    if button_a.was_pressed():
        display.clear()

        # measure the distance in cm
        distanceToObject = sonar.distance_mm() // 10

        # if the distance is below 10 then turn all pixels to red. otherwise turn them green
        if distanceToObject < 10:
            display.scroll(str(distanceToObject) + " cm")
            neopixelStrip[0] = (255, 0, 0)
            neopixelStrip[1] = (255, 0, 0)
            neopixelStrip[2] = (255, 0, 0)
            neopixelStrip[3] = (255, 0, 0)
            neopixelStrip.show()

            # wait 2 seconds then turn them off
            sleep(2000)
            neopixelStrip[0] = (0, 0, 0)
            neopixelStrip[1] = (0, 0, 0)
            neopixelStrip[2] = (0, 0, 0)
            neopixelStrip[3] = (0, 0, 0)
            neopixelStrip.show()
            display.show(Image.HAPPY)
        else:
            display.scroll(str(distanceToObject) + " cm")
            neopixelStrip[0] = (0, 255, 0)
            neopixelStrip[1] = (0, 255, 0)
            neopixelStrip[2] = (0, 255, 0)
            neopixelStrip[3] = (0, 255, 0)
            neopixelStrip.show()

            # wait 2 seconds then turn them off
            sleep(2000)
            neopixelStrip[0] = (0, 0, 0)
            neopixelStrip[1] = (0, 0, 0)
            neopixelStrip[2] = (0, 0, 0)
            neopixelStrip[3] = (0, 0, 0)
            neopixelStrip.show()
            display.show(Image.HAPPY)
