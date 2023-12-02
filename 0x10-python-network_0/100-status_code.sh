#!/bin/bash
# Sends a request and displays only the status code
curl -sI "$1" | awk '/HTTP/ {print $2}'
