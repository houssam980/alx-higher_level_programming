#!/usr/bin/python3
"""
take url
"""

import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as res:
        print(dict(res.headers).get("X-Request-Id"))
