# The MIT License (MIT)
#
# Copyright (c) 2017 Scott Shawcroft for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`adafruit_thermistor` - Read temperature with a thermistor
====================================================

A thermistor is a resistor that varies with temperature. This driver takes the
parameters of that resistor and its series resistor to determine the current
temperature. To hook one up, connect an analog input pin to the connection
between the resistor and the thermistor.

* Author(s): Scott Shawcroft

Implementation Notes
--------------------

**Hardware:**

* Adafruit `10K Precision Epoxy Thermistor - 3950 NTC <https://www.adafruit.com/products/372>`_  (Product ID: 372)

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the ESP8622 and M0-based boards: https://github.com/adafruit/circuitpython/releases

**Notes:**

#. Check the datasheet of your thermistor for the values.
"""

import math
import analogio

class Thermistor:
    """Thermistor driver"""

    def __init__(self, pin, series_resistor, nominal_resistance, nominal_temperature, b_coefficient):
        self.pin = analogio.AnalogIn(pin)
        self.series_resistor = series_resistor
        self.nominal_resistance = nominal_resistance
        self.nominal_temperature = nominal_temperature
        self.b_coefficient = b_coefficient

    @property
    def temperature(self):
        """The temperature of the thermistor in celsius"""
        reading = self.pin.value / 64
        reading = (1023 * self.series_resistor) / reading
        reading -= self.series_resistor

        steinhart = reading / self.nominal_resistance  # (R/Ro)
        steinhart = math.log(steinhart)               # ln(R/Ro)
        steinhart /= self.b_coefficient                # 1/B * ln(R/Ro)
        steinhart += 1.0 / (self.nominal_temperature + 273.15)  # + (1/To)
        steinhart = 1.0 / steinhart               # Invert
        steinhart -= 273.15                       # convert to C

        return steinhart
