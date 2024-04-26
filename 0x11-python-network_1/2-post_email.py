#!/usr/bin/python3
"""send post request to url with an email as parameter"""

import urllib.request
import urllib.parse
import sys


url = sys.argv[1]
email = {"email": str(sys.argv[2])}
data = urllib.parse.urlencode(email)
data = data.encode("ascii")
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as res:
    text = res.read()
    print(text.decode("utf-8"))
