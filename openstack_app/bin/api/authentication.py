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
This script performs authentication and return authentication token and services information
Author: Basant Kumar, GSLab
'''

#Import from standard libraries
import sys
import argparse
import requests
import ConfigParser
import os
import io

def login(user_name,password):
	#Variable declaration
	headers = {'content-type': 'application/json'}
	auth_token = None
	nova_url = None
	auth_response = None
	auth_token = None

	Config = ConfigParser.ConfigParser()
	PATH = os.path.dirname(os.path.realpath(__file__))
	with io.open(PATH+"/./../../local/myconf.conf", 'r', encoding='utf_8_sig') as fp:
		Config.readfp(fp)
	for section in Config.sections():
		if section == 'userinfo':
			for option in Config.options(section):
				if option == 'baseurl':
					base_url = Config.get(section,option)
				if option == 'tenant':
					tenant = Config.get(section,option)
	

	try:
	    auth_request = ('{ "auth": {"identity": {"methods": ["password"],"password": {"user": {"name": "' + user_name + '","domain": { "id": "default" },"password": "' + password + '"}}},"scope": {"project": {"name": "admin","domain": { "id": "default" }}}}}')
	    auth_response = requests.post(base_url + '/auth/tokens', data=auth_request,headers=headers);
	    auth_response_body = auth_response.json();   
	    subject_token = auth_response.headers["x-subject-token"]
	    auth_token = auth_response.headers["x-subject-token"]
	   
        
	    if not auth_response_body['token']['user']['id']:  
	        raise Exception("Authentication failed. Failed to get an auth token.")
	  
	except Exception as e:
	    print ('WARNING: Athentication failed for tenant %s and user %s' 
	           % (tenant, user_name) + '\nInfo: ' + str(e))

	return auth_token,auth_response_body

	

