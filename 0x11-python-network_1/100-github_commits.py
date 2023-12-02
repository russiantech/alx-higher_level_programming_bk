#!/usr/bin/python3
"""
Uses the GitHub API to list 10 commits (from the most recent to oldest)
of a repository by a given user.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    repo_name, owner_name = sys.argv[1], sys.argv[2]
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'
    params = {'per_page': 10}

    try:
        response = requests.get(url, params=params)
        commits = response.json()

        for commit in commits:
            sha = commit.get('sha', '')
            author_name = commit.get('commit', {}).get('author', {}).get('name', '')
            print(f"{sha}: {author_name}")

    except ValueError:
        print("Not a valid JSON")
    except Exception as e:
        print(e)
