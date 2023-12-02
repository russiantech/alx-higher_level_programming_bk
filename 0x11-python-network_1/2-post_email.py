#!/usr/bin/python3
"""
Takes in a URL & an email, 
sends a POST request to the URL with the email as a param,
displays the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    with urllib.request.urlopen(url, data=data) as response:
        print(response.read().decode('utf-8'))
