☁️ AWS Cloud Support Simulator

Hands-on AWS Cloud Support & CloudOps lab for troubleshooting EC2, Lambda, S3, VPC, and GuardDuty incidents using realistic cloud support scenarios. Ideal for Cloud Support, CloudOps, DevOps, and SysOps portfolios.

📝 TL;DR

7 production-grade AWS incident simulations (P0/P1/P2)

Automate and monitor incidents with Python, Terraform, CloudWatch, and AWS CLI

Build portfolio-ready projects demonstrating CloudOps & DevOps skills

Gain hands-on experience aligned with AWS SysOps and Solutions Architect certs

📌 Table of Contents

Purpose

Features

Architecture

Repository Structure

Usage

Screenshots

Learning Outcomes

Portfolio & Career Alignment

Tech Stack

Contributing

Contact

Support

🎯 Purpose

Gain real-world AWS Cloud Support experience by investigating 7 production incidents, demonstrating:

Logs analysis

Metrics monitoring

Incident response

Remediation & prevention

🔥 Features

Production-grade incidents for EC2, Lambda, S3, VPC, GuardDuty

Cloud observability: CloudWatch Logs/Metrics/Dashboards, X-Ray

Security operations: GuardDuty alerts, IAM forensics, CloudTrail investigations

Performance tuning: Lambda & EC2 optimization, DynamoDB capacity planning

Infrastructure as Code: Terraform modules

Automation: Python (boto3), AWS CLI, Bash scripts

Incident reporting: Runbooks & post-mortems

🏗️ Architecture

Multi-Tier VPC Design (2 AZs)

Route 53 → ALB → Web Tier (EC2) → App Tier (EC2 / Lambda) → Database (RDS / DynamoDB)


Public Subnet: ALB, web servers

Private Subnet: App servers, RDS/DynamoDB

Networking: NAT Gateway, IGW, Route Tables, SGs, NACLs, Flow Logs

Monitoring: CloudWatch Logs/Metrics/Alarms/Dashboards, X-Ray

Security: GuardDuty, CloudTrail, IAM, AWS Config

📂 Repository Structure
AWS_Cloud_Support_Sim/
│
├── scenarios/          # 7 Production Incidents
├── cloudwatch/         # Dashboards, Alarms, Log Insights queries
├── scripts/            # Automation tools (health check, cost analysis, remediation)
├── terraform/          # Core IaC modules and environment configs
├── docs/               # Runbooks and troubleshooting guides
└── tests/              # Automated validation tests

⚡ Usage
Prerequisites

AWS Free Tier account

Python 3.9+ with boto3

Terraform v1.0+

AWS CLI v2

Git

Setup & Run
# Clone repo
git clone https://github.com/charles-bucher/AWS_Cloud_Support_Sim.git
cd AWS_Cloud_Support_Sim

# Install dependencies
pip install -r requirements.txt

# Verify tools
terraform --version
aws --version
python --version

Launch First Scenario
cd scenarios/001-ec2-connectivity

# Deploy infrastructure
cd terraform
terraform init
terraform plan -out=tfplan
terraform apply tfplan

# Investigate incident
cat README.md          # Read incident brief
python ../../scripts/validate_fix.py --scenario 001

# Clean up resources after scenario
terraform destroy -auto-approve

🖼️ Screenshots

CloudWatch Dashboard:


Incident Simulation Output:


Terraform Deployed Infrastructure:


🎓 Learning Outcomes

Master VPC networking, Security Groups, NACLs

Troubleshoot Lambda performance & DynamoDB throttling

Conduct CloudTrail forensics & GuardDuty investigations

Automate remediation using Python & Terraform

Build observability stacks with CloudWatch & X-Ray

Optimize cloud cost & performance

💼 Portfolio & Career Alignment

Portfolio Experience Entry:

AWS Cloud Operations Lab | Independent Project | 2025
- Investigated 7 production-grade AWS incidents (P0/P1/P2)
- Built CloudWatch dashboards and automated monitoring scripts
- Optimized Lambda, EC2, and DynamoDB performance
- Conducted security incident response and CloudTrail forensic analysis
- Deployed environments via Terraform IaC


Skills Demonstrated: AWS, CloudOps, Terraform, Python, Observability, Security

Certifications Prep: AWS SAA-C03, AWS SOA-C02

🛠️ Tech Stack

Cloud: AWS (EC2, Lambda, S3, VPC, RDS, DynamoDB, CloudWatch, CloudTrail, GuardDuty)

IaC: Terraform

Automation: Python (boto3), AWS CLI, Bash

Monitoring/Observability: CloudWatch, X-Ray

🤝 Contributing

Fork repo → feature branch → commit → pull request

Suggest new scenarios, scripts, or documentation improvements

📞 Contact

Charles Bucher – CloudOps Engineer | AWS Specialist

GitHub: @charles-bucher

LinkedIn: charles-bucher-cloud

Email: quietopscb@gmail.com

⭐ Support This Project

Star ⭐ on GitHub

Share learning journey on LinkedIn/Twitter

Contribute new scenarios or scripts

🏷️ Keywords

aws cloud-operations devops monitoring lambda terraform s3 dynamodb ec2 vpc cloudwatch guardduty cloudtrail python automation incident-response sre sysops cloud-security performance-optimization iaC infrastructure-as-code cloud-support-engineer portfolio-project