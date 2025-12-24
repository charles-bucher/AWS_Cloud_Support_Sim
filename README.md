AWS Cloud Support Simulation Labs

Hands-on AWS Cloud Support labs for troubleshooting EC2, S3, Lambda, IAM, GuardDuty, Security Groups, and VPC scenarios using real cloud support workflows. Focused on logs, metrics, incident response, remediation, and prevention.

TL;DR

Practice AWS Cloud Support workflows in a realistic lab environment.

Includes 7 core scenarios with prebuilt infrastructure and step-by-step guidance.

Focus on troubleshooting, automation, and root cause analysis.

Ideal for building a cloud support portfolio and preparing for AWS Cloud Support or CloudOps roles.

Quick Start

Clone the repo:

git clone https://github.com/charles-bucher/AWS_Cloud_Support_Sim.git
cd AWS_Cloud_Support_Sim


Optional: Create a Python virtual environment and install dependencies:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt


Explore the scenario folders:

scenarios/
├─ 01_cloudwatch-monitoring-scenario
├─ 02_ec2-troubleshoot-scenario
├─ 03_guardduty-automation-scenario
├─ 04_iam-role-policy-scenario
├─ 05_s3-iam-access-scenario
├─ 06_security-groups-nacl-scenario
├─ 07_vpc-architecture-scenario


Follow the README in each scenario for step-by-step instructions.

Incident Scenarios
ID	Incident	Services	Difficulty	Status
01	EC2 connectivity issues	EC2, CloudWatch	Medium	Active
02	S3 bucket misconfiguration	S3, IAM	Medium	Active
03	GuardDuty alert automation	GuardDuty, Lambda	Hard	Active
04	IAM role & policy misconfig	IAM	Medium	Active
05	S3 bucket IAM access issues	S3, IAM	Medium	Active
06	Security groups & NACL misconfig	EC2, VPC	Medium	Active
07	VPC architecture verification	VPC, Subnets	Medium	Active

Each scenario contains: prebuilt infrastructure, step-by-step instructions, screenshots, and remediation steps.

Skills You’ll Practice

AWS EC2, S3, Lambda, IAM, GuardDuty, VPC

CloudWatch metrics & dashboards

Incident response & troubleshooting workflows

Root cause analysis

Terraform & infrastructure as code (IaC)

Python automation for AWS

Cloud support documentation

Screenshots

00_lab_environment_verified.png

01_vpc_architecture_setup.png

02_vpc_subnets_routing.png

03_security_groups_network_acls.png

04_iam_roles_policies_setup.png

06_s3_bucket_setup.png

07_guardduty_dashboard_overview.png

08_s3_bucket_configuration.png

09_cloudwatch_monitoring_dashboard.png

All screenshots are included in the screenshots/ folder.

Installation

Clone the repo.

Install dependencies (pip install -r requirements.txt) if using Python scripts.

Review scenario README.md files for Terraform setup and execution instructions.

License

This project is licensed under the MIT License — see LICENSE
 for details.

Contact

Charles Bucher
GitHub
 | LinkedIn