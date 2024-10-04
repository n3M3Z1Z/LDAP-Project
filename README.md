# LDAP-Project
A simple and Basic LDAP-Server, and Server hardening


### LDAP Server Setup - hamster.panzer
Project Overview
This repository contains the necessary configuration and setup for an LDAP server hosted on an Ubuntu Biotic virtual machine. The LDAP server is configured for the domain hamster.panzer with an IP address of 192.168.56.100. The project includes pre-configured security services and tools for managing user authentication and system access.

Requirements
Before setting up the LDAP server, ensure you have the following software installed on your local machine:

Vagrant
VirtualBox
These tools are essential for provisioning and managing the virtual machine where the LDAP server and associated services will run.

Setup Instructions
Step 1: Clone the Repository
Start by cloning this repository to your local machine:

git clone https://github.com/n3m3z1z/LDAP-Project.git
cd ldap-server-hamster-panzer
Step 2: Start the Vagrant Environment
The Vagrantfile included in this repository is configured to set up the required virtual environment. To start the environment, run:

vagrant up
This command will download the base Ubuntu Biotic box if not already present and provision the virtual machine with the LDAP server and all required security services.

Step 3: Access the Virtual Machine
Once the Vagrant environment is up, you can start the server VM in Virtualbox.

Step 4: LDAP Server Details
Domain Name: hamster.panzer
IP Address: 192.168.56.100
LDAP Services: No pre-configuration you are free to follow our guide provided in the Documentation.pdf as well as the Guide.pdf
Step 5: Security Software
The following security tools are to be installed, to secure the LDAP-Server:

ClamAV (Antivirus)
Fail2Ban (Brute-force protection)
RKHunter (Rootkit detection)
UFW (Firewall)
AppArmor (Mandatory Access Control)
Snort (Intrusion detection)
Suricata (Network-based IDS/IPS)
Each of these tools has been configured for basic operation. For more detailed configurations and usage instructions, refer to the Documentation.

Hardening and Threat Modeling
Hardening
SSH Configuration: Ensure strong password policies, disable root login, and use key-based authentication.
Firewall Rules: Restrict access to only necessary ports using UFW.
Regular Updates: Keep the system and all software packages updated to minimize vulnerabilities.
User Privileges: Follow the principle of least privilege when assigning user permissions.
Threat Modeling
Identify Assets: User data, authentication mechanisms, and sensitive information stored in the LDAP directory.
Identify Threats: Unauthorized access, data leakage, and service disruptions.
Assess Risks: Evaluate the likelihood and impact of identified threats, and implement appropriate mitigations.
Incident Response Plan
Incident Reporting
Establish a procedure for staff to report security incidents via email.
Email address for incident reports: security@hamster.panzer.
Incident Response Steps
Identification: Confirm the incident and gather relevant information.
Containment: Limit the impact of the incident.
Eradication: Remove the cause of the incident.
Recovery: Restore affected systems and services.
Lessons Learned: Conduct a post-incident review to improve future responses.
Incident Reports
Maintain detailed records of all incidents, including:

Date and time of the incident
Description of the incident
Steps taken in response
Resolution and follow-up actions
Documentation
All PDFs related to this project are currently in German. An English version will follow soon. Please refer to the documentation for in-depth details on the setup and management of the LDAP server.

For further information or questions, please contact the project maintainers.

