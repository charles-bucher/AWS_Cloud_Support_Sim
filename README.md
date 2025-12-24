# AWS Cloud Support Simulator  
**Hands-on Incident-Driven AWS Troubleshooting Labs**

> Realistic Cloud Support scenarios designed to mirror how AWS Support, CloudOps, and SRE teams investigate, remediate, and prevent production incidents.

---

## 🔥 Why This Repo Exists

Most “cloud labs” teach *how to deploy*.  
This project teaches **how to debug when things break**.

**AWS_Cloud_Support_Sim** is a collection of **incident-driven troubleshooting scenarios** based on real-world cloud support workflows:
- Broken infrastructure
- Failing permissions
- Misconfigured security
- Silent monitoring gaps
- Production-style root cause analysis

This repo is built for:
- Cloud Support Engineers
- CloudOps / DevOps Engineers
- SRE-minded practitioners
- Hiring managers reviewing real troubleshooting ability

---

## 🧠 What You’ll Practice Here

- 🔍 Reading logs, metrics, and error messages
- 🧪 Reproducing failures safely
- 🛠️ Applying targeted fixes (not guesswork)
- 📈 Verifying recovery
- 🔁 Preventing recurrence

**No toy examples. No “hello world” labs.**

---

## 🧪 Scenario Coverage

| Category | What Breaks | Skills Tested |
|-------|------------|--------------|
| EC2 | SSH / connectivity failures | VPC, Security Groups, IAM, logs |
| S3 | Access denied & public exposure | IAM policies, bucket policies |
| Lambda | Timeouts & runtime errors | Logs, retries, permissions |
| CloudWatch | Missing alarms & blind spots | Metrics, alerts, dashboards |
| GuardDuty | Security findings | Detection, automation, response |
| Networking | SG vs NACL conflicts | Traffic flow, isolation |
| IAM | Over/under-permissioning | Least privilege, role trust |

Each scenario includes:
- 📄 Incident description
- 🧠 Root cause analysis
- 🛠️ Remediation steps
- 📸 Screenshots / evidence
- ✅ Validation checks

---

## 📂 Repository Structure

AWS_Cloud_Support_Sim/
├── scenarios/ # Incident-based labs
│ ├── ec2-troubleshoot/
│ ├── s3-iam-access/
│ ├── lambda-error/
│ ├── guardduty-automation/
│ └── ...
├── screenshots/ # Visual proof of work
├── diagrams/ # Architecture & flow diagrams
├── scripts/ # Automation & validation tools
├── src/ # Supporting Python utilities
├── tests/ # Scenario & repo validation
├── docs/ # Guides and explanations
└── validate_repos.py # Portfolio quality gate

yaml
Copy code

---

## 🚀 Quick Start

```bash
git clone https://github.com/charles-bucher/AWS_Cloud_Support_Sim.git
cd AWS_Cloud_Support_Sim
Each scenario folder contains:

A README with the incident

Supporting configs or scripts

Screenshots proving resolution

No global deployment required — scenarios are isolated and intentional.

🛠️ Tooling & Tech
AWS: EC2, S3, Lambda, CloudWatch, GuardDuty, IAM, VPC

IaC: Terraform (where appropriate)

Automation: Python, PowerShell

Validation: Custom repo & README validators

Mindset: Support-first, production-aware

📸 Proof, Not Promises
This repo intentionally includes:

Screenshots of failures and fixes

Logs and metrics

Validation scripts

Consistent documentation standards

This is evidence, not claims.

🧩 How This Is Different From Tutorials
Tutorials	This Repo
Deploy-first	Incident-first
Happy path	Broken by design
“Click here”	Diagnose & decide
No evidence	Screenshots & logs
Toy labs	Production mindset

📌 Who This Is For
If you want to:

Break into Cloud Support

Level up troubleshooting confidence

Prove hands-on AWS ability

Show how you think, not just what you deploy

You’re in the right place.

📜 License
MIT License — use freely for learning and inspiration.

🤝 Contributing
See CONTRIBUTING.md if you’d like to extend scenarios or improve tooling.

🔐 Security
See SECURITY.md for responsible disclosure.

📬 Contact
Charles Bucher
GitHub: https://github.com/charles-bucher
LinkedIn: https://www.linkedin.com/in/charles-bucher-cloud

## 📸 Key Scenario Screenshots

Below are selected highlights demonstrating hands-on AWS troubleshooting and operations:

| Scenario | Screenshot |
|----------|------------|
| Lab environment verification | ![Lab Setup](screenshots/00_lab_environment_verified.png) |
| VPC architecture | ![VPC Setup](screenshots/01_vpc_architecture_setup.png) |
| Security Groups & NACLs | ![Network Security](screenshots/03_security_groups_network_acls.png) |
| IAM Roles & Policies | ![IAM Setup](screenshots/04_iam_roles_policies_setup.png) |
| S3 Bucket Setup | ![S3 Setup](screenshots/06_s3_bucket_setup.png) |
| GuardDuty Monitoring | ![GuardDuty Dashboard](screenshots/07_guardduty_dashboard_overview.png) |
| CloudWatch Monitoring | ![CloudWatch Dashboard](screenshots/09_cloudwatch_monitoring_dashboard.png) |

