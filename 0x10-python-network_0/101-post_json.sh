#!/bin/bash
# Sends a JSON POST request to a URL

if [ -f "$2" ] && jq . "$2" >/dev/null 2>&1; then
    curl -s -H "Content-Type: application/json" -d @"$2" "$1"
else
    echo "Not a valid JSON or file does not exist."
fi
