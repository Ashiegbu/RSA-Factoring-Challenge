#!/usr/bin/python3
def read_data(name):
    with open(name) as f:
        contents = f.read()
        contents_ints = [int(x) for x in contents.split()]
        return contents_ints
