
Example snippets
================


Reading measurement value
-------------------------

Start/Stop the measurement and read a single measurement from the sensor.
For multiple reads, the :code:`read()` function could be called multiple times.
However, please note, that the sensor reads the current values only once per second.

The fan has a start-up time of at least three seconds.
Thus it takes some time until the first measurement is available after sending the start command.
To make sure that a value is available, a sleep of five seconds seems to be a good value.
This time is, however, only a recommendation and could be changed if desired.

.. code-block:: python

    from sps30 import SPS30

    port: str = "COM3"
    sps30 = SPS30(port=port)

    sps30.start_measurement()
    time.sleep(5)

    values = sps30.read_values()
    print(values)

    sps30.stop_measurement()


Read the firmware version
----------------------------

Read the major and minor number of the firmware version.
An example output could be :code:`V2.2`.

.. code-block:: python

    from sps30 import SPS30

    port: str = "COM3"
    sps30 = SPS30(port=port)

    firmware_version = sps30.read_firmware_version()
    print(f"Firmware version: V{firmware_version[0]}.{firmware_version[1]}")


Read the status register
---------------------------

The status register of the sensor contains some useful information as for example if the fan has a problem.
Output of the register is however a 32bit unsigned integer number.
For an easier interpretation it is recommended to use the :code:`parse_status_register()` function.
This function extracts the import bits of the register and maps them into a dictionary that allows the access of the important bits by a key.

.. code-block:: python

    from sps30 import SPS30

    port: str = "COM3"
    sps30 = SPS30(port=port)

    status_register = sps30.read_status_register()
    status_register = parse_status_register(status_register)
    print(f"Status register: {status_register}")
