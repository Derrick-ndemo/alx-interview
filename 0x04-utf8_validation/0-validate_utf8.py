#!/usr/bin/python3
"""
UTF-8 encoding
"""


def validUTF8(data):
    count = 0  # to count the bytes which should follow the first byte

    for num in data:
        num = format(num, '#010b')[-8:]  # get the last 8 bits
        if count == 0:
            if num[0] == '0':
                continue
            if num[:3] == '110':
                count = 1
            elif num[:4] == '1110':
                count = 2
            elif num[:5] == '11110':
                count = 3
            else:
                return False
        else:
            if num[:2] != '10':
                return False
            count -= 1
    return count == 0  # return False if the string is unfinished, otherwise True