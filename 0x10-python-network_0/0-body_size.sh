#!/bin/bash
# Takes a URL, sends a request,& displays the size of the response body
curl -so /dev/null "$1" -w '%{size_download}\n'
