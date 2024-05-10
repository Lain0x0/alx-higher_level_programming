#!/usr/bin/python3
""" Sending a request to an URL and display the body of the response """
from urllib import request, error
from sys import argv

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as respond:
            print(respond.read().decode('UTF-8'))
    except error.HTTPError as err:
        print('Error code:', err.code)
