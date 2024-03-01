#!/usr/bin/python3
"""
fetch from alx
"""


if __name__ == '__main__':
    import urllib.request
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        ctn = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(ctn)))
        print("\t- content: {}".format(ctn))
        print("\t- utf8 content: {}".format(ctn.decode('utf-8')))
