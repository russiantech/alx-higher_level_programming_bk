#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status
"""

import urllib.request

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")
