#!/bin/zsh

source ./common.zsh
ansible-playbook -vvvv -i ec2.py -u ubuntu ./rolling_restart.yml
