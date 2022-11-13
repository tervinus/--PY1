from pprint import pprint


def get_dict(number) -> dict:
    number_dict = {
        "bin": bin(number),
        "dec": number,
        "hex": hex(number),
        "oct": oct(number)
    }
    return number_dict


pprint([get_dict(i) for i in range(16)])
