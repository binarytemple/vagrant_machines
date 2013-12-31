These scripts demonstrate creating API request to bitbucket 
============================================================

The longer term goal will be to:

When provisioning a VM from Vagrant using Ansible

Create a SSH key using Ansible 
Register that key into bucket using the Python BitBucket API


Where:

I am creating a VM for my own exclusive development use, on a trusted computer.

I want to be able to check out repositories RW into the VM.

The specific repository I intend to use it first for is my Docker/LXC experiments.

About the Scripts in this directory 

* bitbucket_list_all_ssh_keys.py List all ssh keys for your account
* Registers for OAUTH, deletes all ssh keys under your acc.
* bitbucket_register_oauth.py

Reading Resources  
-------------------


# Bitbucket-API, how to install and use

https://bitbucket-api.readthedocs.org/en/latest/

# The BitBucket-API repo

https://github.com/Sheeprider/BitBucket-api

# My API configuration page
https://bitbucket.org/account/user/binarytemple/api

# Developing Ansible Modules

http://www.ansibleworks.com/docs/developing_modules.html

And the link that inspired it all 

http://www.ansibleworks.com/docs/modules.html#docker
