ansible all -vvvv -i .virtualbox-ansible-hosts -m shell -a "command='/usr/bin/echo ping' register=result  "
