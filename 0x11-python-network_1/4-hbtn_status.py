#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using the requests package.
Displays the body of the response.
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)

    print("Body response:")
    print(f"    - type: {type(response.text)}")
    print(f"    - content: {response.text}")
