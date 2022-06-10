import math
from unittest import result


def decimal_to_binary(decimal_number):
    """Returns the array of digits in binary representation of a decimal number"""
    """ recursiv"""
    # if decimal_number > 1:
    #     decimal_to_binary(decimal_number // 2)
    # print(decimal_number % 2, end='')
    # # print(decimal_number)
    # # return decimal_number
    """ iterativ"""
    # if decimal_number == 0:
    #     return [0]
    # bit = []
    # while decimal_number:
    #     bit.append(decimal_number % 2)
    #     decimal_number >>= 1
    #     print(bit[::-1])
    """
    do-while in python wtf!
    """
    bits = []
    while True:
        divisor = decimal_number // 2
        remainder = decimal_number % 2
        bits.append(remainder)
        decimal_number = divisor
        if divisor == 0:
            break
    return bits

    pass


def binary_to_decimal(binary_digits):
    """Returns the decimal (number) representation of a binary number represented by an array of 0/1 digits"""
    result = 0
    for i, v in enumerate(binary_digits[::-1]):
        result += v * pow(2, i)
    return result

    pass


def decimal_to_base(decimal_number, destination_base):
    """Returns the digits in destination_base representation of the decimal number"""
    if destination_base == 10:
        return decimal_number
    elif destination_base == 2:
        return decimal_to_binary(decimal_number)
    elif destination_base == 8:
        result = []
        list_decimal_digits = [int(x) for x in str(decimal_number)]
        for i, v in enumerate(list_decimal_digits):
            result += v * pow(8, range(i, 0))
            return result
    elif destination_base == 16:
        result_0 = 0
        result_i = 0
        list_decimal = [x for x in decimal_number]
        for i, v in enumerate(list_decimal):
            if i == len(list_decimal):
                result_0 = v * pow(8, 0)
            result_i += v * pow(18, (range(i, 1)))
        return result_0 + result_i
    pass


def base_to_decimal(digits, original_base):
    """Returns the decimal (number) representation of an array of digits given in original_base"""
    nr_digits = [int(x) for x in digits]
    sum = 0
    for i, v in enumerate(nr_digits):
        sum += (len(nr_digits) - 1) * pow(original_base, range(len(nr_digits), 0))
    return sum
    pass


def digits_as_string(digits, base):
    """Returns the string representation of an array of digits given in base"""
    pass
    base_16_dict = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
    }
    for item in digits:
        if item > int(base):
            raise ValueError("input parameter is greater than the base")

    if int(base) < 16:
        string_number = ""
        for item in digits:
            if item < 10:
                string_number += str(item)
            if item >= 10:
                for key, value in base_16_dict.items():
                    if key == item:
                        string_number += value
        return string_number
    else:
        raise ValueError("base is bigger than 16")


def convert_base(original_digits, original_base, destination_base):
    """Conversion from any base to any other base"""
    base_dict = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
        16: "G",
        17: "H",
        18: "I",
        19: "J",
    }
    if original_base == 2 or original_base == 16 or original_base == 8:
        if destination_base == 10:
            decimal_nr = 0
            for item in range(len(original_digits)):
                for key in base_dict:
                    ''' finds the number by key'''
                    if base_dict[key] == original_digits[::-1][item]: 
                        decimal_nr += key * (original_base ** item)
            return (f'Decimal number: {decimal_nr}')
    if original_base == 10:
        if original_digits == "0":
            another_base_nr = 0
        else:
            another_base_nr = ""
            while decimal_nr > 0:
                ''' finds the corresponding value'''
                another_base_nr += base_dict[decimal_nr % destination_base] 
                decimal_nr = int(decimal_nr / destination_base)
        return (f' Base {destination_base} number is {another_base_nr[::-1]}')
    pass


def main():
    # print(decimal_to_binary(20))
    # print(binary_to_decimal([1, 0, 1, 0, 0]))
    # print(decimal_to_base(20, 8))
    base = input("Please, enter a number < = 16\n")
    print(digits_as_string([2, 15, 9, 11], base))


if __name__ == "__main__":
    main()
