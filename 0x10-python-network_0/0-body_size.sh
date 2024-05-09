#!/bin/bash
# Writing a bash scripts that take and URL sends a REQUEST to that URL
# And showing the size of of the body of the response
url=$1
if [ $# -eq 1 ]
then
	curl -s -w "%{size_download}\n" -o /dev/null $url
fi

