#!/bin/bash
# Script take URL, send requst to URL, display size of body response
curl -sI "$1" | grep 'Content-Length:' | cut -f2 -d' '
