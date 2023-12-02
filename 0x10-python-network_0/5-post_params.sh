#!/bin/bash
# make POST request & displays the response body
curl -sX POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
