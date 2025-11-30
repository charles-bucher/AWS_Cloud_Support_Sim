⚡ AWS Cloud Support Simulation (Hands-On Troubleshooting Lab)










A complete AWS Cloud Support & CloudOps simulation designed to demonstrate real troubleshooting skills, root-cause analysis, automation, monitoring, and infrastructure management.

This repository was built to align with Cloud Support Engineer, NOC Engineer, CloudOps, and Site Support roles.

🧩 Project Overview

This repo simulates the actual workflow used in Cloud Support environments:

Incident intake → analysis → resolution → validation

Debugging AWS services (EC2, S3, IAM, Lambda)

Identifying system misconfigurations and network issues

Automating CloudOps tasks with Python

Validating infrastructure with Terraform / CloudFormation

Documenting reproducible fixes

Recruiters can evaluate CloudOps competency directly from this repo.

🚀 Core Skills Demonstrated
✔ Cloud Support & Troubleshooting

SSH failures, network reachability, EC2 access

IAM permission debugging

S3 access issues

Lambda execution failures

Log and metric interpretation (CloudWatch)

✔ Automation

Python scripting for operational tasks

Log parsing, validation, CLI automation

Dependency management (requirements.txt)

✔ Infrastructure as Code

Terraform provisioning

CloudFormation deployment & validation

✔ Monitoring & Logging

AWS CloudWatch: metrics, alarms, logs

Diagnostic workflow: identify → isolate → remediate

✔ DevOps Practices

Git version control

GitHub Actions

Repo organization, code quality, documentation

This layout is designed for ATS keyword detection and quick recruiter scanning.

🏗️ Architecture Diagram

This flow illustrates the lifecycle of every troubleshooting scenario in this repo—incident → RCA → remediation → verification.

📂 Scenario Catalog (Recruiter View)
1️⃣ EC2 Troubleshooting Scenario

Objectives:

Deploy EC2 via CloudFormation

Verify provisioning

Fix Security Group rules

Restore SSH connectivity

Document RCA + resolution steps

Screenshots:




2️⃣ Python Automation Scenario

Objectives:

Run Python-based operational tasks

Use scripts for log validation

Automate repetitive CloudOps steps

Screenshots:




🔧 How to Run the Lab
# Clone the repository
git clone https://github.com/charles-bucher/AWS_Cloud_Support_Sim.git

# Install Python dependencies
pip install -r requirements.txt

# (Optional) Deploy sample AWS infrastructure
terraform init
terraform apply


Then select a scenario from /scenarios and follow the documented troubleshooting path.

🎯 Role Alignment

This project is aligned with the responsibilities of:

AWS Cloud Support Associate / Engineer

NOC Analyst / NOC Technician

Cloud Support Specialist

Cloud Operations Engineer (CloudOps)

L1/L2 Technical Support (Cloud Focus)

Your repo demonstrates:

Incident diagnosis

Real AWS debugging

Automation mindset

Infrastructure validation

Documentation discipline

Production support awareness

Exactly what recruiters look for.

🔥 Career Objective

Build a portfolio of hands-on, validated Cloud Support scenarios that show:

AWS troubleshooting competency

Python and automation capability

Infra reliability thinking

Log-based debugging

Endpoint + network diagnostics

Infrastructure-as-code workflow usage

This repo is intentionally crafted to be recruiter-ready and ATS-friendly.

📬 Contact

GitHub: https://github.com/charles-bucher

LinkedIn: https://www.linkedin.com/in/charles-bucher-cloud

Email: quietopscb@gmail.com

📝 Additional Notes

All scenarios mirror real Cloud Support incident patterns

AWS resources may incur cost — destroy when finished

