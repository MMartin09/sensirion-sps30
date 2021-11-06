import time

from sps30 import SPS30


def main():
    port: str = "/dev/ttyUSB0"

    sps30 = SPS30(port=port)

    #    firmware_version = sps30.read_firmware_version()
    #    print(f"Firmware version: V{firmware_version[0]}.{firmware_version[1]}")

    sps30.start_measurement()
    time.sleep(1.5)

    for i in range(10):
        values = sps30.read_values()
        print(values)
        time.sleep(1)

    sps30.stop_measurement()


if __name__ == "__main__":
    main()
