#!/usr/bin/python3

def uppercase(str):
    if isinstance(str, int):
        print("{}".format(str))
        return

    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            print("{}".format(chr(ord(char) - 32)), end="")
        else:
            print("{}".format(char), end="")
    print()
