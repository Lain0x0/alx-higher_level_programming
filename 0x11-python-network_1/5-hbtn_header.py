#!/usr/bin/python3
""" Using requests to the URL and display
the value of the variable X-Request-Id """
from sys import argv
import requests


if __name__ == "__main__":
    respond = requests.get(argv[1])
    print(respond.headers.get('X-Request-Id'))
