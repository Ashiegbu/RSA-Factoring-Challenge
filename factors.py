#!/usr/bin/python3
import sys
from read_data import read_data

data = read_data(sys.argv[1])
maximmum = max(data)
minimum = min(data)


def prime_num_generator():
    primeN = []
    for num in range(2, 100):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primeN.append(num)
    return primeN


primeNumbers = prime_num_generator()


def mul(a, b):
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] % b[j] == 0:
                x = a[i] // b[j]
                print("{}={}*{}".format(a[i], x, b[j]))
                break


mul(data, primeNumbers)
