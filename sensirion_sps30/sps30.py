import struct
import time
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

    def start_measurement(self) -> None:
        """Starts the measurement."""
        self.conn.write([0x7E, 0x00, 0x00, 0x02, 0x01, 0x03, 0xF9, 0x7E])

    def stop_measurement(self) -> None:
        """Stops the measurement."""
        self.conn.write([0x7E, 0x00, 0x01, 0x00, 0xFE, 0x7E])

    def read_values(self) -> Tuple:
        """Reads the measured values.

        The output data structure consists of 10 big-endian float IEEE754 values.
        For further information see the documentation.

        Returns:
            The read values.

        """

        self.conn.reset_input_buffer()

        self.conn.write([0x7E, 0x00, 0x03, 0x00, 0xFC, 0x7E])

        in_bytes = self.conn.in_waiting
        while in_bytes < 47:
            in_bytes = self.conn.in_waiting
            time.sleep(0.1)

        raw_data = self.conn.read(in_bytes)

        raw_data = reverse_byte_stuffing(raw_data)
        raw_data = trim_data(raw_data)

        data = struct.unpack(">ffffffffff", raw_data)

        return data

    def read_product_type(self) -> str:
        """Reads the product type of the sensor.

        The type of the sensor is always equal to "00080000".
        If the value is different maybe the wrong port has been selected.

        Returns:
            Product type as string.

        """

        self.conn.reset_input_buffer()

        self.conn.write([0x7E, 0x00, 0xD0, 0x01, 0x00, 0x2E, 0x7E])

        in_bytes = self.conn.in_waiting
        while in_bytes < 16:
            in_bytes = self.conn.in_waiting
            time.sleep(0.1)

        raw_data = self.conn.read(in_bytes)

        raw_data = reverse_byte_stuffing(raw_data)
        raw_data = trim_data(raw_data)

        # Remove null character
        raw_data = raw_data[:-1]

        # Unpack the raw data
        data = raw_data.decode("ascii")

        return data

    def read_serial_number(self) -> str:
        """Reads the serial number of the sensor.

        Returns:
            Serial number as string with maximal length of 32 ASCII characters.

        """

        self.conn.reset_input_buffer()

        self.conn.write([0x7E, 0x00, 0xD0, 0x01, 0x03, 0x2B, 0x7E])

        in_bytes = self.conn.in_waiting
        while in_bytes < 24:
            in_bytes = self.conn.in_waiting
            time.sleep(0.1)

        raw_data = self.conn.read(in_bytes)

        raw_data = reverse_byte_stuffing(raw_data)
        raw_data = trim_data(raw_data)

        # Remove null character
        raw_data = raw_data[:-1]

        # Unpack the raw data
        data = raw_data.decode("ascii")

        return data

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

        raw_data = reverse_byte_stuffing(raw_data)
        raw_data = trim_data(raw_data)

        # Unpack the raw data
        data = struct.unpack(">bbbbbbb", raw_data)

        firmware_major: int = data[0]
        firmware_minor: int = data[1]

        return firmware_major, firmware_minor

    def read_status_register(self) -> int:
        """Read the status register of the device.

        For further information about the status register, see the documentation.

        Returns:
            Current status register as 32bit unsigned integer.

        """

        self.conn.reset_input_buffer()

        self.conn.write([0x7E, 0x00, 0xD2, 0x01, 0x00, 0x2C, 0x7E])

        in_bytes = self.conn.in_waiting
        while in_bytes < 12:
            in_bytes = self.conn.in_waiting
            time.sleep(0.1)

        raw_data = self.conn.read(in_bytes)

        raw_data = reverse_byte_stuffing(raw_data)
        raw_data = trim_data(raw_data)

        # Unpack the raw data
        data = struct.unpack(">Ib", raw_data)

        # Extract the register (Byte 4 is unused)
        register: int = data[0]

        return register


def reverse_byte_stuffing(raw_data) -> bytes:
    """Apply reverse byte-stuffing on an input byte string.

    See the documentation for more information.

    Args:
        raw_data (bytes): Input bytes to be replaced.

    Returns:
        The input data with reversed byte-stuffed characters.

    """

    if b"\x7D\x5E" in raw_data:
        raw_data = raw_data.replace(b"\x7D\x5E", b"\x7E")
    if b"\x7D\x5D" in raw_data:
        raw_data = raw_data.replace(b"\x7D\x5D", b"\x7D")
    if b"\x7D\x31" in raw_data:
        raw_data = raw_data.replace(b"\x7D\x31", b"\x11")
    if b"\x7D\x33" in raw_data:
        raw_data = raw_data.replace(b"\x7D\x33", b"\x13")

    return raw_data


def trim_data(raw_data) -> bytes:
    """Removes head and tail from byte string.

    Args:
        raw_data: Input bytes to be trimmed.

    Returns:
        Trimmed data string.
    """

    return raw_data[5:-2]
