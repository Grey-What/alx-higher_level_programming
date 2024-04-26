#!/usr/bin/python3
"""
takes a letter and url as argument
sent post request to url with letter as parameter
evaluate response to json file and print formated output
"""

import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    try:
        q = sys.argv[1]
    except IndexError:
        q = ""

    payload = {'q': q}

    r = requests.post(url, data=payload)

    try:
        string = r.json()
        if len(string) != 0:
            print("[{}] {}".format(string.get("id"), string.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
