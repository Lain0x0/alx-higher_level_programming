#!/usr/bin/python3
""" Using requests and sys to take URL and an EMAIL address
send a POST request to the parsed URL """
from sys import argv
import requests


if __name__ == "__main__":
    value = {'email': argv[2]}
    respond = requests.post(argv[1], data=value)
    print(respond.text)
