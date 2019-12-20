#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        val = [1, 5, 10, 50, 100, 500, 1000]
        rom = ["I", "V", "X", "L", "C", "D", "M"]
        result = 0
        prev = 1001
        for i in range(len(roman_string)):
            idx = rom.index(roman_string[i])
            if prev >= val[idx]:
                result = result + val[idx]
                prev = val[idx]
            else:
                result = val[idx] - 2 * prev + result
                prev = val[idx]
        return result
    else:
        return 0
