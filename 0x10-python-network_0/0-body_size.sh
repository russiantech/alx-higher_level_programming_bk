#!/bin/bash
# Takes a URL, sends a request,& displays the size of the response body

#curl -sI "$1" | grep -i Content-Length | awk '{print $2}' | tr -d '\r'
curl -so /dev/null "$1" -w '%{size_download}\n'
