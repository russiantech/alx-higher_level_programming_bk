#!/usr/bin/python3
"""
Takes GitHub credentials (username & personal access token) and uses the GitHub API
to display the user's id. Basic Authentication with a personal access token is used.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    username, token = sys.argv[1], sys.argv[2]
    url = 'https://api.github.com/user'

    try:
        response = requests.get(url, auth=(username, token))
        data = response.json()
        print(data.get('id', 'None'))

    except ValueError:
        print("Not a valid JSON")
    except Exception as e:
        print(e)
