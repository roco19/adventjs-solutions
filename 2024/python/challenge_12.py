VALUES_MAP = {
    "*": 1,
    "o": 5,
    "^": 10,
    "#": 50,
    "@": 100,
}


# Challenge
def calculate_price(ornaments: str) -> int:
    try:
        total = 0
        for i in range(len(ornaments)):
            curr_ornament = ornaments[i]

            curr_value = VALUES_MAP[curr_ornament]
            if i + 1 < len(ornaments) and curr_value < VALUES_MAP[ornaments[i + 1]]:
                total -= curr_value
            else:
                total += curr_value
        return total
    except KeyError:
        return "undefined"


if __name__ == "__main__":
    print(calculate_price("***"))
    print(calculate_price("*o"))
    print(calculate_price("o*"))
    print(calculate_price("*o*"))
    print(calculate_price("**o*"))
    print(calculate_price("o***"))
    print(calculate_price("*o@"))
    print(calculate_price("*#"))
    print(calculate_price("@@@"))
    print(calculate_price("#@"))
    print(calculate_price("#@Z"))
