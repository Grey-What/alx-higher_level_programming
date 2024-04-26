#!/usr/bin/python3
"""fetch a url with urllib"""

import urllib.request as urlreq


if __name__ == "__main__":
    req = urlreq.Request("https://alx-intranet.hbtn.io/status")
    with urlreq.urlopen(req) as res:
        text = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(text)))
        print("\t- content: {}".format(text))
        print("\t- utf8 content: {}".format(text.decode("utf-8")))
