from typing import Dict


def parse_status_register(register) -> Dict[str, int]:
    """Parse the status register into a dict.

    Args:
        register (int): Status register as 32 bit unsigned integer.

    Returns:
        Register bits as a dictionary.

    **Keys:**

        * fan_speed: Bit 21
        * laser_failure: Bit 5
        * fan_failure: Bit 4

    Please note, `fan_failure` and `laser_failure` are Errors and `fan_speed` a Warning.
    For further information see the documentation.

    """

    data = {"fan_speed": 0, "laser_failure": 0, "fan_failure": 0}

    # if the register is 0 everything is ok
    if register == 0:
        return data

    if is_set(register, 4):
        data["fan_failure"] = 1

    if is_set(register, 5):
        data["laser_failure"] = 1

    if is_set(register, 21):
        data["fan_speed"] = 1

    return data


def is_set(n, b) -> int:
    """Checks if a bit is set.

    Args:
        n (int): Input number.
        b (int): Bit that should be checked.

    Returns:
        True if the `b`-th bit is set in `n`. False otherwise.

    """

    return n & 1 << b
