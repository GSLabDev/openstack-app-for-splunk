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
This script fetches user credentails from Splunk endpoints
Author:  Basant Kumar, GSLab
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

class credential:
    def __init__(self, app_name, user_name):
        #Initialize class variables
        self.app_name = app_name
        self.user_name = user_name
        self.password = ""

    def getPassword(self, session_key):
        import splunk.entity as entity
        import urllib
	
        if len(session_key) == 0:
            raise Exception, "No session key provided"
        if len(self.app_name) == 0:
            raise Exception, "No app provided"
        try:
            entities = entity.getEntities(['admin', 'passwords'], namespace=self.app_name, owner='nobody', sessionKey=session_key)
        except Exception, e:
            raise Exception, "Could not get %s credentials from splunk. Error: %s" % (self.app_name, str(e))
        for i, c in entities.items():
            return c['username'], c['clear_password']
        raise Exception, "No credentials have been found"
