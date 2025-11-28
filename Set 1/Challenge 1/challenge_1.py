#!/usr/bin/env python3

# Standard library imports
from base64 import b64encode


def get_flag() -> str:
    """
    Returns the challenge flag https://www.cryptopals.com/sets/1/challenges/1

    :return: Flag
    """

    hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

    # If the input is 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d,
    # the output should be SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t.
    flag = b64encode(bytes.fromhex(hex_string)).decode()

    return flag


if __name__ == "__main__":
    print(get_flag())
