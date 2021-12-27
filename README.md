# Sensirion SPS30 PM Sensor

![PyPI](https://img.shields.io/pypi/v/sensirion-sps30?style=flat-square)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/MMartin09/sensirion-sps30/lint?style=flat-square)
![GitHub](https://img.shields.io/github/license/MMartin09/sensirion-sps30?style=flat-square)
[![style black](https://img.shields.io/badge/Style-Black-black.svg?style=flat-square)](https://github.com/ambv/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat-square&labelColor=ef8336)](https://pycqa.github.io/isort/)

## Usage

Example Python script to read and print a single measurement.

```python
from time import sleep

from sensirion_sps30 import SPS30

port: str = "COM3"
sps30 = SPS30(port)

sps30.start_measurement()
sleep(5)

data = sps30.read_values()
print(data)

sps30.stop_measurement()
```