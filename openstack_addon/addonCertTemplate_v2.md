# Proposed Add-on Certification Documentation Template
**November 2014**

All content listed in the table of contents is _required_.
——-

## Template Table of Contents

### OVERVIEW

- About the OpenStack Add-on for Splunk
- Release notes
- Support and resources

### INSTALLATION AND CONFIGURATION

- Hardware and software requirements
- Installation steps
- Deploy to single server instance
- Deploy to distributed deployment
- Deploy to distributed deployment with Search Head Pooling
- Deploy to distributed deployment with Search Head Clustering
- Deploy to Splunk Cloud 
- Configure OpenStack Add-on for Splunk

### USER GUIDE

- Data types
- Lookups

---
### OVERVIEW

#### About the OpenStack Add-on for Splunk

| Author | Basant Kumar, GSLab |
| --- | --- |
| App Version | 2.0 |
| Vendor Products | OpenStack Newton |
| Has index-time operations | false |
| Create an index | false |
| Implements summarization | false |

The OpenStack Add-on for Splunk allows a Splunk® Enterprise administrator to collect service status and resource usage information. This information is used by the OpenStack App for Splunk to show OpenStack cloud status. Make sure that you install OpenStack App for Splunk on Splunk server.

##### Scripts and binaries

| Script | Purpose |
| --- | --- |
| execute.sh | Shell script to execute python script with parameters |
| get_service_status.py | Fetches service status information, requires service name as parameter  |
| system_status.py | Gets resouce usage information |

#### Release notes

##### About this release

Version 2.0 of the OpenStack Add-on for Splunk is compatible with:

| Splunk Enterprise versions | 6.5.1 |
| --- | --- |
| Platforms | Requires Linux |
| Vendor Products | OpenStack Newton |
| CIM | NA |
| Lookup file changes | NA |

##### New features

OpenStack Add-on for Splunk includes the following new features:

- Not Applicable.

##### Fixed issues

Version 2 of the OpenStack Add-on for Splunk fixes the following issues:

- Not Applicable.

##### Known issues

Version 1.0 of the OpenStack Add-on for Splunk has no known issues.

##### Third-party software attributions

Version 2 of the OpenStack Add-on for Splunk incorporates the following third-party software or libraries.

- Not Applicable.

##### Support and resources

**Questions and answers**

- Not Applicable.

**Support**

Report issues to splunk@gslab.com.
Hours of operations: 9 hours a day (04:30 - 13:30 UTC).
Saturday, Sunday are holidays.
Response time user should expect when they report an issue: within 12 hours.
Initially, issues will be tracked using the email thread. If the issue is found to be a valid bug, it will be moved to a bug tracking system.

## INSTALLATION AND CONFIGURATION

### Hardware and software requirements

#### Hardware requirements

OpenStack Add-on for Splunk supports the following server platforms in the versions supported by Splunk Enterprise:

- Ubuntu 16.04 (or later)
- CentOS 7 (or later)
- Fedora 20 (or later)

#### Software requirements

To function properly, OpenStack App for Splunk requires the following software:

- Python 2.7 

#### Splunk Enterprise system requirements

Because this add-on runs on Splunk Enterprise, all of the [Splunk Enterprise system requirements](http://docs.splunk.com/Documentation/Splunk/latest/Installation/Systemrequirements) apply.

#### Download

Download the OpenStack Add-on for Splunk from Splunkbase.

#### Installation steps

To install and configure this app on your supported platform, follow these steps:

**Install to forwarders**

1. Ensure that the Splunk Forwarder is installed.
2. Ensure that the Splunk Forwarder is not running. If it is running, shut it down by running $SPLUNK_HOME/bin/splunk stop.
3. In $SPLUNK_HOME/etc/apps/openstack_addon/default/inputs.conf, enable required inputs by setting disabled=0.
4. At the begining of inputs.conf there is a default stanza which includes openstack, node_type, node tags. Here, in 'openstack', specify your OpenStack Newton deployment type, e.g. Production, Testing, Development,Staging etc. In 'node_type', you need to specify type of the current node e.g. controller, cinder, compute, neutron, etc. In 'node', specify the name of that node e.g. compute_node_1, compute_ubuntu_node, compute_docker, etc. These tags are used by the Splunk server to uniquely identify each node.
5. Start the Splunk Forwarder by running $SPLUNK_HOME/bin/splunk start.

##### Deploy to single server instance

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

#### Configure OpenStack Add-on for Splunk

- In $SPLUNK_HOME/etc/apps/openstack_addon/default/inputs.conf, enable required inputs by setting disabled=0.
- At the begining of inputs.conf there is a default stanza which includes openstack, node_type, node tags. Here:
  - In 'openstack', specify your OpenStack Newton deployment type, e.g. Production, Testing, Development,Staging etc.
  - In 'node_type', you need to specify type of the current node e.g. controller, cinder, compute, neutron, etc.
  - In 'node', specify the name of that node e.g. compute_node_1, compute_ubuntu_node, compute_docker, etc.

## USER GUIDE

### Data types

This app provides the index-time and search-time knowledge for the following types of data from OpenStack Newton:

**Data type**

- Sourcetype = Log files
  - OpenStack Add-on for Splunk collects log information and Splunk forwarder forwards that information to Splunk server. These log files includes linux syslog, Auth log, NTP log and other log files specific to OpenStack Newton setup.

- Sourcetype = Scripted inputs
  - OpenStack Add-on for Splunk collects system status information using scripted inputs. This information includes CPU, RAM, Disk usage, service status information.


These data types support the following Common Information Model data models:

- Not Applicable.

### Lookups

The OpenStack Add-on for Splunk contains1 lookup files.

- Not Applicable.