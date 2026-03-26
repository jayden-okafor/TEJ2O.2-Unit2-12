/* Copyright (c) 2026 MTHS All rights reserved
 *
 * Created by: Jayden Okafor
 * Created on: Mar 2026
 * This program turns all the pixels colour to red if the distance is below 10cm. and turns them green if distance is above 10cm
*/

let neopixelStrip: neopixel.Strip = null
let distanceToObject: number = 0

basic.clearScreen()

neopixelStrip = neopixel.create(DigitalPin.P16, 4, NeoPixelMode.RGB)

// turn all 4 pixels off
neopixelStrip.setPixelColor(0, neopixel.colors(NeoPixelColors.Black))
neopixelStrip.setPixelColor(1, neopixel.colors(NeoPixelColors.Black))
neopixelStrip.setPixelColor(2, neopixel.colors(NeoPixelColors.Black))
neopixelStrip.setPixelColor(3, neopixel.colors(NeoPixelColors.Black))
neopixelStrip.show()

input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    
    // measure the distance in cm
    distanceToObject = sonar.ping(
        DigitalPin.P1, // trigger
        DigitalPin.P2, // echo
        PingUnit.Centimeters,
    )

    if (distanceToObject < 10) {

    } else {

    }
})