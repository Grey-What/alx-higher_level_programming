#!/usr/bin/python3
"""
takes url and email then sent POST request with email as parameter
display body of response
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    val = {'email': sys.argv[2]}

    r = requests.post(url, data=val)

    print(r.text)
