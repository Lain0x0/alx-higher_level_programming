#!/usr/bin/python3
""" Using urllib and sys to send a REQUEST to URL
and display the value of the X-Request-Id """
from urllib import request
from sys import argv


if __name__ == "__main__":
    with request.urlopen(argv[1]) as url_req:
        data = url_req.headers.get("X-Rrquest-Id")
        print(data)
