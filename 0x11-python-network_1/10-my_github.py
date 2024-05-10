#!/usr/bin/python3
""" Using GitHub API to display your ID by using requests and sys """
from sys import argv
from requests.auth import HTTPBasicAuth
import requests


if __name__ == "__main__":
    credentials = HTTPBasicAuth(argv[1], argv[2])
    respond = requests.get("https://api.github.com/user", auth=credentials)
    print(respond.json().get("id"))
