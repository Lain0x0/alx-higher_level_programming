#!/bin/bash
# Writing a bash scripts that take and URL sends a REQUEST to that URL
# And showing the size of of the body of the response
curl -s "$1" | wc -c

