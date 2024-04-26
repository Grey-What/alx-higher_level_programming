#!/usr/bin/python3
"""
takes url, then send get request
Display body of response decoded into utf-8
"""

import urllib.error
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        res = urllib.request.urlopen(req)
        print(res.read().decode('ascii'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
