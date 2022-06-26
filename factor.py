#!/usr/bin/python3

import sys


def factor(n):
    numb = int(n)
    mul = 0
    if num < 4:
        print("{:d}={:d}*1".format(num, num))
        return
    for i in range(2, num):
        if num % i == 0:
            mul = num // i
            break
    print("{:d}={:d}*{:d}".format(num, value, mul))


if len(sys.argv) != 2:
    print("Usage: factors <file>")
    sys.exit()
filename = sys.argv[1]
try:
    nums = open(filename, "r")
except FileNotFoundError:
    print("Error: Can't open file <{:s}>".format(filename))
    sys.exit()

for num in nums:
    factor(num)

nums.close()
