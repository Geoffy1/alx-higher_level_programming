#!/bin/bash
# takes in a URL, sends a request to that URL
curl -sI "$1" | wc -c
