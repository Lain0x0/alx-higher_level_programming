#!/usr/bin/python3
""" Using urllib and sys to send a REQUEST to URL
and display the value of the X-Request-Id """
from urllib import request
import sys

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)
