import adafruit_thermistor
import board
import time

# these values work with the Adafruit CircuitPlayground Express.
# they may work with other thermistors as well, as they're fairly standard,
# though the pin will likely need to change (ie board.A1)
pin = board.TEMPERATURE
series_resistor = 10000
nominal_resistance = 10000
nominal_temperature = 25
b_coefficient = 3950
high_side_bool = True

thermistor = adafruit_thermistor.Thermistor(pin, series_resistor, nominal_resistance, nominal_temperature, b_coefficient, high_side=high_side_bool)

# print the temperature in C and F to the serial console every second
while True:
    celsius = thermistor.temperature
    fahrenheit = (celsius * 9 / 5) + 32
    print('== Temperature ==\n{} *C\n{} *F\n'.format(celsius, fahrenheit))
    time.sleep(1)
