#!/bin/zsh

source ./common.zsh
ansible-playbook -vvvv -i ec2.py -u ubuntu ./basho_keys_to_all_ec2.yml
