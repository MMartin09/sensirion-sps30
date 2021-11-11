import time

from helper import parse_status_register

from sensirion_sps30 import SPS30


def main():
    port: str = "COM3"

    sps30 = SPS30(port=port)

    product_type = sps30.read_product_type()
    print(f"Product type: {product_type}")

    serial_number = sps30.read_serial_number()
    print(f"Serial number: {serial_number}")

    firmware_version = sps30.read_firmware_version()
    print(f"Firmware version: V{firmware_version[0]}.{firmware_version[1]}")

    status_register = sps30.read_status_register()
    status_register = parse_status_register(status_register)
    print(f"Status register: {status_register}")

    # sensirion_sps30.start_measurement()
    # time.sleep(3.5)
    #
    # for i in range(10):
    #     values = sensirion_sps30.read_values()
    #     pretty_print(values)
    #     time.sleep(1)
    #
    # sensirion_sps30.stop_measurement()


def pretty_print(data) -> None:
    for i in range(len(data)):
        print(f"{data[i]:.2f} ", end="")
    print("")


if __name__ == "__main__":
    main()
