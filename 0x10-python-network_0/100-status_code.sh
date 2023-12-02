#!/bin/bash
# Sends a request to a URL and displays the status code
curl -w'%{response_code}' "$1" -so /dev/null
