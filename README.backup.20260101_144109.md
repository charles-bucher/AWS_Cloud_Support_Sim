# ☁️ AWS Cloud Support Simulator

![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen)
![Last Commit](https://img.shields.io/github/last-commit/charles-bucher/AWS_Cloud_Support_Sim)

![AWS](https://img.shields.io/badge/AWS-SysOps%20Administrator-orange)
![CloudOps](https://img.shields.io/badge/Role-Cloud%20Support%20%7C%20CloudOps-blue)
![Terraform](https://img.shields.io/badge/IaC-Terraform-623CE4)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB)

![CloudWatch](https://img.shields.io/badge/Monitoring-CloudWatch-success)
![Incident](https://img.shields.io/badge/Incident%20Response-P0--P2-critical)
![IaC](https://img.shields.io/badge/Infrastructure-As%20Code-blueviolet)

---

## 📌 TL;DR
**Production-style AWS Cloud Support lab** simulating real-world incidents, alarms, and remediation workflows aligned to the **AWS SysOps Administrator** and **Cloud Support Associate** role.

This project demonstrates:
- Monitoring & alerting (CloudWatch)
- Incident response (P0–P2 scenarios)
- Root cause analysis
- Infrastructure as Code (Terraform)
- Automation & operational scripting (Python)

Built to reflect **on-call CloudOps work**, not toy demos.

---

## 🧭 Overview
AWS_Cloud_Support_Sim is a hands-on simulation environment designed to mirror the daily responsibilities of an AWS Cloud Support / Cloud Operations engineer.

The lab intentionally introduces **misconfigurations, failures, and degraded states** so the operator must:
- Detect issues via monitoring
- Diagnose root causes
- Apply fixes using AWS-native tooling and IaC
- Document remediation steps clearly

This repo prioritizes **operational realism over theory**.

---

## 🏗 Architecture

**Core AWS Services Used**
- EC2 (compute workloads & failure simulation)
- CloudWatch (metrics, alarms, logs)
- IAM (least-privilege roles)
- VPC (basic networking context)
- S3 (logs & artifacts)

**Tooling**
- Terraform → infrastructure provisioning & drift control  
- Python → automation, checks, remediation helpers  
- YAML → configuration & workflows  

**High-Level Flow**
1. Terraform provisions infrastructure
2. Faults are introduced (manual or scripted)
3. CloudWatch alarms trigger
4. Investigation & remediation occurs
5. Resolution is documented

---

## 🧪 Scenarios Covered
- EC2 CPU / memory saturation
- Misconfigured security groups
- IAM permission failures
- Missing or broken CloudWatch alarms
- Infrastructure drift detection
- Log-based troubleshooting

Each scenario reflects **real AWS Support ticket patterns**.

---

## ▶️ Usage

### Prerequisites
- AWS account (free tier is sufficient)
- AWS CLI configured
- Terraform ≥ 1.x
- Python 3.9+

### Deploy Infrastructure
```bash
terraform init
terraform apply
Trigger a Scenario
Follow scenario instructions in /scenarios

Observe CloudWatch alarms

Investigate metrics & logs

Remediate
Apply fixes manually or via Terraform/Python

Validate alarm recovery

Document resolution steps

📸 Screenshots (Examples)
Screenshots intentionally reflect real operator views

CloudWatch alarm firing

EC2 metrics during incident

Terraform plan/apply output

Incident resolution confirmation

📁 See /screenshots directory.

📁 Repository Structure
text
Copy code
.
├── terraform/        # Infrastructure as Code
├── scripts/          # Python automation & helpers
├── scenarios/        # Incident simulations
├── screenshots/     # Evidence & visuals
├── docs/             # Runbooks & explanations
└── README.md
🎯 Skills Demonstrated (SysOps-Aligned)
AWS Monitoring & Alerting

Incident Response (P0–P2)

Root Cause Analysis (RCA)

Infrastructure as Code

Change management mindset

Clear technical documentation

This repo is designed to answer:

“Can this person handle production cloud issues?”

🚀 Why This Matters
Most portfolios show what AWS services are.
This project shows how to operate them under pressure.

That’s the difference between studying cloud and working cloud.

📄 License
MIT License — free to use, modify, and learn from.

👤 Author
Charles Bucher
AWS Cloud Support | CloudOps
Focused on troubleshooting, automation, and production readiness

yaml
Copy code


## Tech Stack
- AWS (EC2, VPC, S3, IAM, Lambda)
- Infrastructure as Code (Terraform)
- Monitoring & Logging (CloudWatch, CloudTrail)
- Security & Compliance (GuardDuty, AWS Config)
- Python (boto3)



## Cost Considerations
This project was built with cost-awareness in mind:
- Free tier–safe resource sizing
- Explicit teardown steps included
- Logging scoped to avoid unnecessary ingestion costs
- Monitoring configured to balance visibility vs spend

> Demonstrates real-world cloud cost responsibility.



## Operational Responsibility & Risk Mitigation
This lab simulates production support responsibilities:
- Incident-driven troubleshooting
- Security signal investigation (GuardDuty findings)
- Audit visibility via CloudTrail and Config
- Infrastructure reproducibility using Terraform

This reflects SysOps-style ownership, not tutorial-only usage.

