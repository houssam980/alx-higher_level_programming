#!/bin/bash
# get size of the body of the response
curl -s "$1" | wc -c
