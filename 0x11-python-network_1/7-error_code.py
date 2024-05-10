#!/usr/bin/python3
""" Using requests and sys to send request to the URL
the body of the response """
from sys import argv
import requests


if __name__ == "__main__":
    respond = requests.get(argv[1])
    try:
        respond.raise_for_status()
        print(respond.text)
    except Exception as err:
        print("Error code: {}".format(respond.status_code))
