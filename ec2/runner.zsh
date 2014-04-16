#!/bin/zsh

eval `sed -n  '/aws_secret_access_key/{s_[^=]*=__;s_ *__;s/.*/export AWS_SECRET_KEY=&/;p;}' < ~/.boto`
eval `sed -n '/aws_access_key_id/{s_[^=]*=__;s_ *__;s/.*/export AWS_ACCESS_KEY=&/;p;}' < ~/.boto`
export ANSIBLE_HOST_KEY_CHECKING=False

/common/ansible/bin/ansible-playbook -vvvv -i local boot.yml
