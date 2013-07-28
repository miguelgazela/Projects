# Binary to Decimal and Back Converter
# Develop a converter to convert a decimal number to binary 
# or a binary number to its decimal equivalent.

def binary_to_decimal(binary):
    decimal = 0
    i = 0

    while binary > 0:
        binary, last_digit = divmod(binary, 10)

        if last_digit not in [0,1]:
            raise ValueError

        decimal += last_digit * (2**i)
        i += 1

    return decimal

def decimal_to_binary(decimal):
    binary = []

    while decimal > 0:
        decimal, remainder = divmod(decimal, 2)
        binary.append(remainder)

    binary.reverse()

    res = ""
    for digit in binary:
        res += str(digit)

    return int(res)

def main():
    print binary_to_decimal(110000)
    print decimal_to_binary(48)


if __name__ == "__main__":
    main()