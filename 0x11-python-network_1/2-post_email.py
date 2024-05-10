#!/usr/bin/python3
""" script that takes in a URL and an email,
sends a POST request to the passed URL """
from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    values = {'email': argv[2]}
    data_val = parse.urlencode(values).encode('utf-8')
    req = request.Request(argv[1], data_val)
    with request.urlopen(req) as reqy:
        print(reqy.read().decode('utf-8'))
