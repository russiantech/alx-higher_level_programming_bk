#!/bin/bash
# POST request to the URL with specific parameters & displays the response body

curl -sX POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
