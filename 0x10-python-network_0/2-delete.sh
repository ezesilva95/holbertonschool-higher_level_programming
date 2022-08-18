#!/bin/bash
#script that sends DELETE reqst to URL passed as first argmnt and displays body response
curl -sX DELETE "$1"
