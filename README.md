# Sensirion SPS30 PM Sensor

![PyPI](https://img.shields.io/pypi/v/sensirion-sps30?style=flat-square)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/MMartin09/sensirion-sps30/lint?style=flat-square)
![GitHub](https://img.shields.io/github/license/MMartin09/sensirion-sps30?style=flat-square)
[![style black](https://img.shields.io/badge/Style-Black-black.svg?style=flat-square)](https://github.com/ambv/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat-square&labelColor=ef8336)](https://pycqa.github.io/isort/)

## Short description

<a href="https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Pictures/1_Products/Particulate_Matter/Sensirion_PM_Sensors_SPS30_580x290.png">
    <img src="https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Pictures/1_Products/Particulate_Matter/Sensirion_PM_Sensors_SPS30_580x290.png" align="left" height="73" width="145" >
</a>  

This is a simple library to communicate with a [Sensirion SPS30](https://www.sensirion.com/en/environmental-sensors/particulate-matter-sensors-pm25/) sensor via Serial communication. 
The SPS30 is an MCERTS-certified particulate matter sensor based on laser scattering measurement principles. 
It can classify particles within PM1.0, PM2.5, PM4 and PM10 categories. 

For further details refer to the official [documentation](https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/9.6_Particulate_Matter/Datasheets/Sensirion_PM_Sensors_Datasheet_SPS30.pdf) of the sensor.

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

## Contributions

Community contributions are a welcome addition to the project. 
Before introducing any major features or changes to the existing API please consider opening an [issue](https://github.com/MMartin09/sensirion-sps30/issues) to outline your proposal.

Bug reports are also welcome on the [issue page](https://github.com/MMartin09/sensirion-sps30/issues).
