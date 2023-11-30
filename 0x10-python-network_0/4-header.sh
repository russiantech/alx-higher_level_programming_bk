#!/bin/bash
# GET request to the URL with a custom header&displays the response body

curl -sH "X-School-User-Id: 98" "$1"
