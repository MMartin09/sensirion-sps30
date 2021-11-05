import time
import struct
from typing import Tuple

import serial


class SPS30:
    """Sensirion SPS30.

    Attributes:
        port (str): Serial port of the SPS30.

    """

    def __init__(self, port):
        """

        Args:
            port (str): Serial port of the SPS30.

        """

        self.port: str = port
        self.conn = serial.Serial(self.port, baudrate=115200, stopbits=1, parity="N")

    def read_firmware_version(self) -> Tuple[int, int]:
        """Reads firmware version of the sensor.

        Returns:
            Firmware version as tuple (major, minor).

        """

        self.conn.reset_input_buffer()

        self.conn.write([0x7E, 0x00, 0xD1, 0x00, 0x2E, 0x7E])

        in_bytes = self.conn.in_waiting
        while in_bytes < 14:
            in_bytes = self.conn.in_waiting
            time.sleep(0.1)

        raw_data = self.conn.read(in_bytes)

        if b"\x7D\x5E" in raw_data:
            raw_data = raw_data.replace(b"\x7D\x5E", b"\x7E")
        if b"\x7D\x5D" in raw_data:
            raw_data = raw_data.replace(b"\x7D\x5D", b"\x7D")
        if b"\x7D\x31" in raw_data:
            raw_data = raw_data.replace(b"\x7D\x31", b"\x11")
        if b"\x7D\x33" in raw_data:
            raw_data = raw_data.replace(b"\x7D\x33", b"\x13")

        # Head and tail can be removed
        raw_data = raw_data[5:-2]

        # Unpack the raw data
        data = struct.unpack(">bbbbbbb", raw_data)

        firmware_major: int = data[0]
        firmware_minor: int = data[1]

        return firmware_major, firmware_minor
