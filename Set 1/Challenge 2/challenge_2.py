#!/usr/bin/env python3

def fixed_xor(string1: str, string2: str) -> str:
    """
    A function takes two equal-length buffers and produces their XOR combination.

    :param string1: First string
    :param string2: Second string
    :return: XOR of two equal-length strings
    """

    byte_string1 = bytes.fromhex(string1)
    byte_string2 = bytes.fromhex(string2)

    result = bytearray()
    for b1, b2 in zip(byte_string1, byte_string2):
        result.append(b1 ^ b2)

    xored_string = result.hex()

    return xored_string


def get_flag() -> str:
    """
    Returns the challenge flag https://www.cryptopals.com/sets/1/challenges/2

    :return: Flag
    """

    first_string = "1c0111001f010100061a024b53535009181c"
    second_string = "686974207468652062756c6c277320657965"

    flag = fixed_xor(string1=first_string, string2=second_string)

    assert flag == "746865206b696420646f6e277420706c6179", "Wrong flag, try again."

    return flag


if __name__ == "__main__":
    print(get_flag())
