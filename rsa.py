#!/usr/bin/python3
from read_data import read_data
import math
import sys


data = read_data(sys.argv[1])


def max_prime_number(a):
    max_prime = 0
    """converting the number to odd"""
    while a % 2 == 0:
        max_prime = 2
        a = a / 2
    """ prime factors and replacing maxPrimeFactor"""
    for i in range(3, int(math.sqrt(a)) + 1, 2):
        while a % i == 0:
            max_prime = i
            a = a / i
    if a > 2:
        max_prime = a

    return int(max_prime)


max_p_num = max_prime_number(data[0])


def mul(num, prime_factor):
    x = num // prime_factor
    print("{}={}*{}".format(num, prime_factor, x))


mul(data[0], max_p_num)
