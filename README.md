# Sensirion SPS30 PM Sensor

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Usage

Example Python script to read and print a single measurement.

```python
from time import sleep

from sps30 import SPS30

port: str = "COM3"   # Serial port of the sensor
sps30 = SPS30(port)

sps30.start_measurement()
sleep(1.5)           # Wait until the sensor is ready

data = sps30.read_values()
print(data)

sps30.stop_measurement()
```