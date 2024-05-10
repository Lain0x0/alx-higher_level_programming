#!/usr/bin/python3
""" Fetching an URL {"https://alx-intranet.hbtn.io/status"}"""
from urllib import request


if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as respond:
        fetch = respond.read()
        print("Body response:")
        print("\t- type: {}".format(type(fetch)))
        print("\t- content: {}".format(fetch))
        print("\t- utf8 content: {}".format(fetch.decode("utf-8")))
