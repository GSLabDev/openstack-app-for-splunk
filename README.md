# openstack-app-for-splunk

Openstack App for Splunk

Copyright (c) 2017, Great Software Laboratory Private Limited.

Contributor: Vikas Sanap [vikas.sanap@gslab.com], Basant Kumar [basant.kumar@gslab.com]

https://github.com/GSLabDev/openstack-app-for-splunk

The OpenStack App for Splunk can help by collecting run-time metrics from every node in the Openstack setup and giving you a comprehensive view of the current state of the setup. With this app, you will be able to:
- Gain complete visibility into your OpenStack cloud,
- Search across logs from the entire setup in real-time,
- Troubleshoot and analyze your OpenStack cloud setup with rich, interactive views and more.

Openstack App for Splunk is licensed under the Open Source License.

Client Application

OTPManager will act as Authenticator server whereas Google Authenticator application (available for iOS, Android, BlackBerry and Windows ) as a client to generates OTP code.

Library Documentation

This library includes full JavaDoc documentation and an example code to understand implementation of OTPManager library in a better way.
Usage
Requirements ( build dependencies )

* Python 2.7
* Modify $SPLUNK_HOME/etc/system/default/limits.conf, set max_searches_per_cpu = 6

Instructions
Build

Download zip folder from the url : https://github.com/GSLabDev/openstack-app-for-splunk.git

It will create the 'openstack-app-for-splunk-master.zip' file under Download directory.Extract the folder and follow the installation steps to install.

Usage
-----
The OpenStack App for Splunk fetches cloud setup information from OpenStack APIs. This includes information related to VMs, Images, Networks, Routers, Volumes, etc. In addition to this, with the OpenStack Add-on for Splunk, it shows the status of services, resouce usage and logs from all OpenStack nodes where the Add-on is installed.

Support
-------
   * Report issues to splunk@gslab.com.
   * Hours of operations: 9 hours a day (04:30 - 13:30 UTC).
   * Saturday, Sunday are holidays.
   * Response time user should expect when they report an issue: within 12 hours.
   * Initially, issues will be tracked using the email thread. If the issue is found to be a valid bug, it will be moved to a bug tracking system.

