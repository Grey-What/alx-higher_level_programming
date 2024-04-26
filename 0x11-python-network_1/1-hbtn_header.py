#!/usr/bin/python3
"""accepts url and send request, then display value of header variable"""

import urllib.request as urlreq
import urllib.response as urlres
import sys


if __name__ == "__main__":
    req = urlreq.Request(sys.argv[1])
    with urlreq.urlopen(req) as res:
        print(res.info()["X-Request-Id"])
