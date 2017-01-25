# Proposed App Certification Documentation Template
**November 2014**

All content listed in the table of contents is _required_.
——-

## Template Table of Contents

### OVERVIEW

- About the OpenStack App for Splunk
- Release notes
- Performance benchmarks
- Support and resources

### INSTALLATION

- Hardware and software requirements
- Installation steps 
- Deploy to single server instance
- Deploy to distributed deployment
- Deploy to distributed deployment with Search Head Pooling
- Deploy to distributed deployment with Search Head Clustering
- Deploy to Splunk Cloud 


### USER GUIDE

- Key concepts
- Data types
- Lookups
- Configure OpenStack App for Splunk
- Troubleshooting
- Upgrade
- Example Use Case-based Scenario

---
### OVERVIEW

#### About the OpenStack App for Splunk

| Author | Basant Kumar, GSLab |
| --- | --- |
| App Version | 2.0 |
| Vendor Products | OpenStack Newton |
| Has index-time operations | false |
| Create an index | false |
| Implements summarization | false |

The OpenStack App for Splunk allows a Splunk® Enterprise administrator to monitor and manage an OpenStack cloud setup. OpenStack App for Splunk can collect run-time metrics from every host in your Openstack setup. With the OpenStack App for Splunk, you will be able to gain complete visibility into your OpenStack cloud, search across logs from the entire setup in real-time, troubleshoot and analyze your OpenStack cloud setup with rich, interactive views and more.

##### Scripts and binaries

| Script | Purpose |
| --- | --- |
| app_setup.py | List and store OpenStack user account details |
| agents_info.py | Get OpenStack neutron agents information in JSON format |
| agent_stats.py | Get OpenStack neutron agent statistics |
| authentication.py | Performs user authentication to fetch information from OpenStack APIs |
| credentials.py | Get user credentials stored in the passwords endpoint |
| dict_operations.py | Performs python dictionary operations |
| flavors_info.py | Get OpenStack flavors information in JSON format |
| flavors_stats.py | Get OpenStack flavors statistics |
| hosts_info.py | Get OpenStack compute hosts information in JSON format |
| hypervisors_info.py | Get OpenStack hypervisors information in JSON format |
| hypervisors_stats.py | Get OpenStack hypervisors statistics |
| images_info.py | Get OpenStack VM images information in JSON format |
| images_stats.py | Get OpenStack VM images statistics |
| instances_info.py | Get OpenStack VM instances information in JSON format |
| instances_stats.py | Get OpenStack VM instances statistics |
| networks_info.py | Get OpenStack networks information in JSON format |
| networks_stats.py | Get OpenStack networks statistics |
| routers_info.py | Get OpenStack routers information in JSON format |
| routers_stats.py | Get OpenStack routers statistics |
| services_info.py | Get OpenStack services information in JSON format |
| volumes_info.py | Get OpenStack volumes information in JSON format |
| volumes_stats.py | Get OpenStack volumes statistics |

#### Release notes

##### About this release

Version 2.0 of the OpenStack App for Splunk is compatible with:

| Splunk Enterprise versions | 6.5.1 |
| --- | --- |
| CIM | NA |
| Platforms | Requires Ubuntu Linux 16.04 (or later) or Windows 7 (or later) |
| Vendor Products | OpenStack Newton |
| Lookup file changes | NA |

##### New features

OpenStack App for Splunk includes the following new features:

- Not Applicable.

##### Fixed issues

- Not Applicable.

##### Known issues

- Version 2.0 of the OpenStack App for Splunk has no known issues.

##### Third-party software attributions

- Not Applicable

#### Performance benchmarks

- Not Applicable

##### Support and resources

**Questions and answers**

- Not Applicable

**Support**

Report issues to splunk@gslab.com.
Hours of operations: 9 hours a day (04:30 - 13:30 UTC).
Saturday, Sunday are holidays.
Response time user should expect when they report an issue: within 12 hours.
Initially, issues will be tracked using the email thread. If the issue is found to be a valid bug, it will be moved to a bug tracking system.


## INSTALLATION AND CONFIGURATION

### Hardware and software requirements

#### Hardware requirements

OpenStack App for Splunk supports the following server platforms in the versions supported by Splunk Enterprise:

- Ubuntu 16.04 (or later)
- Windows 7 (or later)

#### Software requirements

To function properly, OpenStack App for Splunk requires the following software:

- Python 2.7 

#### Splunk Enterprise system requirements

Because this add-on runs on Splunk Enterprise, all of the [Splunk Enterprise system requirements](http://docs.splunk.com/Documentation/Splunk/latest/Installation/Systemrequirements) apply.

#### Download

Download the OpenStack App for Splunk from Splunkbase.

#### Installation steps

To install and configure this app on your supported platform, follow these steps:

1. Make sure that Splunk (6.5.0 or above) is running.
2. Login to Splunk with Administrator credentials.
3. Go to the Apps tab.
4. Go to 'Browse more apps' page.
5. Search for 'OpenStack App for Splunk'.
6. Click on the 'Install' button.
7. Stop the Splunk server by running $SPLUNK_HOME/bin/splunk stop.
8. In $SPLUNK_HOME/etc/apps/openstack_app/default/inputs.conf, enable required inputs by setting disabled=0.
9. Start the Splunk server again by running $SPLUNK_HOME/bin/splunk start.
10. Install and configure OpenStack Add-on for Splunk using instructions given in the README file of the Add-on.
11. Access the OpenStack App for Splunk from Apps list. If you are doing this for the first time, you will see a Setup page.
12. On the Setup page, enter valid OpenStack credentials, OpenStack setup details and click on 'Save'.
13. Make sure that OpenStack controller machine's dns entry(i.e. <IP>   <hostname>) is present in Splunk server's dns(i.e. hosts) file.

##### Deploy to single server instance

Follow these steps to install the app in a single server instance of Splunk Enterprise:

- Not Applicable.

##### Deploy to distributed deployment

**Install to search head**

- Not Applicable.

**Install to indexers**

- Not Applicable.

**Install to forwarders**

- Not Applicable.

##### Deploy to distributed deployment with Search Head Pooling
- Not Applicable.

##### Deploy to distributed deployment with Search Head Clustering
- Not Applicable.

##### Deploy to Splunk Cloud
- Not Applicable.

## USER GUIDE

### Key concepts for OpenStack App for Splunk

- OpenStack App for Splunk collects information from the OpenStack Newton APIs and the OpenStack Add-on for Splunk.
- In the App user interface there are two types of pages:
  - Home Page: Displays OpenStack Newton setup health. This information includes cluster health, Networking, Compute and Controller information.
  - Details Pages: These include Compute, Controller, Cinder, Neutron Pages. On each of these pages it displays information related to particular components of OpenStack.

### Data types

This app provides the index-time and search-time knowledge for the following types of data from OpenStack Newton:

**Data type**

- Sourcetype = Scripted inputs
OpenStack App for Splunk collects information from OpenStack Newton APIs using scripts. This includes information related to OpenStack Newton services. e.g Images, Flavors, Neutron Agents, Instances, Networks, etc.

These data types support the following Common Information Model data models:

- Not Applicable.

### Lookups

The OpenStack App for Splunk contains 0 lookup files.

** Lookupname**

- Not Applicable.

### Configure OpenStack App for Splunk

 - When you access the OpenStack App for Splunk make sure that you provide your OpenStack Newton setup details which include user name and password, domain name and the OpenStack horizon base url.
 - If you want to update this configuration, go to the 'Apps' page and click on the 'Setup' link for the OpenStack App for Splunk and edit the configuration.
 - Edit $SPLUNK_HOME/etc/apps/openstack_app/default/inputs.conf file and set disabled = 0 for the appropriate input stanzas marked by comments in the file.

### Troubleshoot OpenStack App for Splunk

***Problem***
OpenStack monitoring information is not displayed on home page
***Cause***
The App is not configured correctly
***Resolution***
- Go to $SPLUNK_HOME/etc/apps/openstack_app/default/inputs.conf and verify that appropriate input stanzas are enabled.
- Verify that you have provided valid admin user credentials and other details on app setup page. Go to App -> Setup page and check configuration.

***Problem***
OpenStack monitoring information is not displayed on compute, controller and other pages
***Cause***
Splunk server or the Openstack Add-on is not configured correctly
***Resolution***
- Splunk server: 
  - Go to Forwarding and receiving page and check that port is configured to receive data from Splunk forwarder.
- Add-on: 
  - Go to $SPLUNK_HOME/etc/apps/openstack_addon/default/inputs.conf and verify that appropriate input stanzas are enabled.
  - Splunk forwarder is running.

### Upgrade OpenStack App for Splunk
- Not Applicable.

### Example Use Case ###
Start and configure OpenStack App for Splunk:
- Start the Splunk server.
- Access the Splunk server home page.
- Download the 'OpenStack App for Splunk' archive from Splunkbase and go to Upload on the app page.
or
- Go to Browse more apps page and search OpenStack App for Splunk, click on install button to install the app.
- Stop the Splunk server.
- Go to $SPLUNK_HOME/etc/apps/openstack_app/default/inputs.conf and set disabled = 0 for appropriate input stanzas.
- Start the Splunk server.
- Access the Splunk server home page.
- From the Apps list, access OpenStack App for Splunk. This will redirect you to Setup page.
- Enter your OpenStack admin account details including tenant name, user name, OpenStack horizon base url, password and click on save button.
- This will redirect your to OpenStack App for Splunk home page.
- Make sure that you install OpenStack Addon for Splunk on OpenStack nodes.