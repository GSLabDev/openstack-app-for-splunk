'''

Openstack Add-on for Splunk 

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
This script to check status of specified service
Arguments: service_name
Author: Basant Kumar, GSLab
'''

#Import from standard libraries
import commands
import time
import datetime
import os
import sys

#Variable declaration
status = 'unrecognized service'
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

#Select tool to get service status details
command_check_code, command_check_output = commands.getstatusoutput("command -v systemctl")
if command_check_code == 0:
	service_status_command_code, service_status_command_output = commands.getstatusoutput(command_check_output+" is-active "+str(sys.argv[1]))
	if service_status_command_code == 0 and 'active' in service_status_command_output:
		status = 'running'
		code = 0
	else:
		status = 'stopped'
		code = 1
else:
	service_status_command_code, service_status_command_output = commands.getstatusoutput("/usr/sbin/service "+str(sys.argv[1])+" status")
	ps_command_code, ps_command_output = commands.getstatusoutput("ps -A")
	if sys.argv[1] in ps_command_output or 'running' in service_status_command_output:
	        status = 'running'
	        code = 0   
	else:
	        status = 'stopped'
	        code = 1
print "timestamp="+st+",service_name=\""+str(sys.argv[1])+"\",error_code=\""+str(code)+"\",service_status=\""+status+"\""
