'''

Openstack App for Splunk 

Copyright (c) 2017, Great Software Laboratory Private Limited.
All rights reserved.

Contributor: Vikas Sanap [vikas.sanap@gslab.com], Basant Kumar [basant.kumar@gslab.com]

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the "Great Software Laboratory Private Limited" nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''

#!/usr/bin/python
'''
This script fetches volumes stats information from OpenStack API
Author: Basant Kumar, GSLab
'''

#Import from standard libraries
import sys
import argparse
import requests
from authentication import *
from pprint import pprint
import json
import os

#Import from own classes
from dict_operations import *
from credentials import *

def main():
        #Variable declaration
        app_name = 'openstack_app'
        user_name = ''
	password = ''
        session_key = sys.stdin.readline().strip()
        splunk_credential = credential(app_name,user_name)
        user_name,password = splunk_credential.getPassword(session_key)
        base_url = ''
        available_volume_count = 0
        inuse_volume_count = 0
        available_volume_size = 0
        inuse_volume_size = 0

        auth_token,auth_services = login(user_name,password)
        for service in auth_services['token']['catalog']:
        	if 'cinder' in service['name']:
        		base_url =  service['endpoints'][2]['url']
        		break
        headers = {'content-type': 'application/json','X-Auth-Token':auth_token}
        response = requests.get(base_url + '/volumes/detail?all_tenants=true',headers=headers).json();
        for volume in response['volumes']:
            if volume['status'] == 'available':
                available_volume_count = available_volume_count + 1
                available_volume_size = available_volume_size + volume['size']
            elif volume['status'] == 'in-use':
                inuse_volume_count = inuse_volume_count + 1
                inuse_volume_size = inuse_volume_size + volume['size']
        
        #Print console line with volumes stats information
        print "available_volume_count="+str(available_volume_count)+",inuse_volume_count="+str(inuse_volume_count)+",inuse_volume_size="+str(inuse_volume_size)+",available_volume_size="+str(available_volume_size)

if __name__ == "__main__":
    main()
