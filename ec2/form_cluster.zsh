#!/bin/zsh

eval `sed -n  '/aws_secret_access_key/{s_[^=]*=__;s_ *__;s/.*/export AWS_SECRET_KEY=&/;p;}' < ~/.boto`
eval `sed -n '/aws_access_key_id/{s_[^=]*=__;s_ *__;s/.*/export AWS_ACCESS_KEY=&/;p;}' < ~/.boto`
export ANSIBLE_HOST_KEY_CHECKING=False

if [[ ( ! -e ./roles ) || ( ! -e ./roles/basho.riak ) || ( ! -e  ./roles/basho.riak-common )  ]] 
then 
	ansible-galaxy install -r roles.txt -p roles
fi

ansible-playbook -vvvv -i ec2.py -u ubuntu ./form_cluster.yml
