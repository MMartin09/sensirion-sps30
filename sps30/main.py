import time

from sps30 import SPS30


def main():
    port: str = "/dev/ttyUSB0"

    sps30 = SPS30(port=port)

    firmware_version = sps30.read_firmware_version()
    print(f"Firmware version: V{firmware_version[0]}.{firmware_version[1]}")

    sps30.start_measurement()
    time.sleep(2.5)

    for i in range(10):
        values = sps30.read_values()
        pretty_print(values)
        time.sleep(1.1)

    sps30.stop_measurement()


def pretty_print(data) -> None:
    for i in range(len(data)):
        print(f"{data[i]:.2f} ", end="")
    print("")


if __name__ == "__main__":
    main()
