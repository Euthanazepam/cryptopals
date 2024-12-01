from base64 import b64encode


def get_flag() -> str:
    """
    Returns the challenge flag https://www.cryptopals.com/sets/1/challenges/1

    :return: Flag
    """

    hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

    flag = b64encode(bytes.fromhex(hex)).decode()

    return flag


if __name__ == "__main__":
    print(get_flag())
