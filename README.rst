
Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-thermistor/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/thermistor/en/latest/
    :alt: Documentation Status

.. image :: https://badges.gitter.im/adafruit/circuitpython.svg
    :target: https://gitter.im/adafruit/circuitpython?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge
    :alt: Gitter

Thermistors are resistors that predictably change resistance with temperature.
This driver uses an analog reading and math to determine the temperature. They
are commonly used as a low cost way to measure temperature.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Usage Example
=============

The hardest part of using the driver is its initialization. Here is an example
for the thermistor on the Circuit Playground and Circuit Playground Express. Its
a 10k series resistor, 10k nominal resistance, 25 celsius nominal temperature and
3950 B coefficient.

.. code-block : python

  import adafruit_thermistor
  import board
  thermistor = adafruit_thermistor.Thermistor(board.TEMPERATURE, 10000, 10000, 25, 3950)
  print(thermistor.temperature)

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_thermistor/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

API Reference
=============

.. toctree::
   :maxdepth: 2

   api
