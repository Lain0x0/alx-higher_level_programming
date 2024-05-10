#!/usr/bin/python3
""" Fetch a URL by using requests """
import requests


if __name__ == "__main__":
    x = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(x.text)))
    print("\t- content: {}".format(x.text))
