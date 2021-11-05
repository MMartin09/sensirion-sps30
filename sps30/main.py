from sps30 import SPS30


def main():
    port: str = "COM3"

    sps30 = SPS30(port=port)
    firmware_version = sps30.read_firmware_version()

    print(f"Firmware version: V{firmware_version[0]}.{firmware_version[1]}")


if __name__ == "__main__":
    main()
