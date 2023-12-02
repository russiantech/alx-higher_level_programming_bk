#!/usr/bin/python3
"""
Takes in a URL, sends a request, & displays the value of the X-Request-Id in the header.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)
