#!/bin/bash -v

./ec2.py | jsonpipe | sed -n '/security_group_rtcloud\/[0-9]/{s/[^"]*//;s_"*__g;p;}' | while read i; do ssh "ubuntu@$i" "sudo apt-get upgrade -y" ; done
