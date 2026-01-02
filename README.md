# AWS Cloud Support Simulator 🚀

[![AWS](https://img.shields.io/badge/AWS-Cloud-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
[![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)](https://www.terraform.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE.md)

> **Real-world AWS troubleshooting scenarios demonstrating Cloud Support Engineer skills**

A hands-on portfolio project simulating production AWS Cloud Support incidents. Demonstrates troubleshooting methodology, infrastructure automation, and operational best practices for entry-level cloud roles.

---

## 📋 Table of Contents

- [About This Project](#about-this-project)
- [Skills Demonstrated](#skills-demonstrated)
- [Architecture](#architecture)
- [Lab Scenarios](#lab-scenarios)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Learning Journey](#learning-journey)
- [Contact](#contact)

---

## 🎯 About This Project

This repository showcases my ability to troubleshoot and resolve real-world AWS infrastructure issues using a Cloud Support Engineer mindset. Each scenario follows industry-standard incident response workflows:

✅ **Problem Identification** → Investigation → Root Cause Analysis → Remediation → Prevention

Built to demonstrate readiness for:
- AWS Cloud Support Associate roles
- Junior SysOps Administrator positions  
- Cloud Operations Engineer roles
- Technical Support Engineer (Cloud) positions

---

## 💼 Skills Demonstrated

### AWS Services
- **Compute:** EC2 (troubleshooting instance connectivity, SSH issues, performance)
- **Storage:** S3 (bucket policies, encryption, access denied errors)
- **Serverless:** Lambda (execution failures, IAM permissions, timeout errors)
- **Security:** IAM (policy troubleshooting, least privilege), GuardDuty (threat detection)
- **Monitoring:** CloudWatch (logs analysis, metrics, alarms configuration)
- **Networking:** VPC, Security Groups, Route Tables, Internet Gateways

### Technical Skills
- Infrastructure as Code (Terraform)
- Python automation scripts
- Log analysis and debugging
- Incident response workflows
- Documentation and ticketing mindset
- Root cause analysis

---

## 🏗️ Architecture

### High-Level Environment Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         AWS Cloud                                │
│                                                                   │
│  ┌──────────────┐        ┌──────────────┐       ┌─────────────┐│
│  │   VPC        │        │  CloudWatch  │       │   GuardDuty ││
│  │              │        │              │       │             ││
│  │  ┌────────┐  │        │  - Logs      │       │  - Alerts   ││
│  │  │  EC2   │  │───────▶│  - Metrics   │───────▶│  - Findings ││
│  │  │Instance│  │        │  - Alarms    │       │             ││
│  │  └────────┘  │        └──────────────┘       └─────────────┘│
│  │              │                                                │
│  │  ┌────────┐  │        ┌──────────────┐                       │
│  │  │  S3    │  │        │   Lambda     │                       │
│  │  │ Bucket │  │        │   Function   │                       │
│  │  └────────┘  │        └──────────────┘                       │
│  │              │                                                │
│  │  ┌────────┐  │                                                │
│  │  │  IAM   │  │        Deployed via Terraform                 │
│  │  │ Roles  │  │                                                │
│  │  └────────┘  │                                                │
│  └──────────────┘                                                │
└─────────────────────────────────────────────────────────────────┘
```

### Scenario Flow Example

```
┌─────────────┐      ┌──────────────┐      ┌─────────────┐      ┌──────────────┐
│   Alert     │─────▶│ Investigation│─────▶│  Root Cause │─────▶│  Remediation │
│  Received   │      │   & Logs     │      │   Analysis  │      │  & Testing   │
└─────────────┘      └──────────────┘      └─────────────┘      └──────────────┘
                            │                      │                     │
                            ▼                      ▼                     ▼
                     CloudWatch Logs        IAM Policy Issue      Updated Policy
                     Error Messages         Missing Permissions   Function Success
```

![Architecture Diagram](diagrams/architecture-overview.png)

---

## 🔧 Lab Scenarios

Each scenario includes: Problem → Investigation → Solution → Validation

### 1️⃣ EC2 Connectivity Issues

**Problem:** Unable to SSH into EC2 instance  
**Investigation:**
- Checked Security Group rules (port 22 blocked)
- Verified Network ACLs
- Confirmed instance has public IP
- Reviewed route table configuration

**Solution:**
```bash
# Added inbound rule for SSH (port 22)
# Source: My IP / 0.0.0.0/0 (for demo purposes)
```

**Result:** ✅ Successfully connected via SSH

![EC2 Troubleshooting](screenshots/ec2-connectivity-fix.png)

---

### 2️⃣ S3 Access Denied Errors

**Problem:** Application receiving `403 Access Denied` when accessing S3 bucket  
**Investigation:**
- Reviewed S3 bucket policy
- Checked IAM role attached to EC2
- Analyzed CloudWatch logs
- Verified encryption settings

**Solution:**
```json
{
  "Effect": "Allow",
  "Action": ["s3:GetObject", "s3:PutObject"],
  "Resource": "arn:aws:s3:::my-bucket/*"
}
```

**Result:** ✅ Application successfully reading/writing to S3

![S3 Access Fix](screenshots/s3-access-denied-resolved.png)

---

### 3️⃣ Lambda Function Timeout

**Problem:** Lambda function timing out after 3 seconds  
**Investigation:**
- Reviewed CloudWatch Logs for error patterns
- Analyzed function execution time metrics
- Checked memory allocation
- Identified inefficient database queries

**Solution:**
- Increased timeout from 3s to 30s
- Optimized code logic
- Added connection pooling

**Result:** ✅ Function completing in < 5 seconds

![Lambda Fix](screenshots/lambda-timeout-resolved.png)

---

### 4️⃣ IAM Permission Errors

**Problem:** Service unable to write logs to CloudWatch  
**Investigation:**
- Reviewed IAM policy attached to role
- Checked trust relationship
- Verified CloudWatch log group exists

**Solution:**
```json
{
  "Effect": "Allow",
  "Action": [
    "logs:CreateLogGroup",
    "logs:CreateLogStream",
    "logs:PutLogEvents"
  ],
  "Resource": "arn:aws:logs:*:*:*"
}
```

**Result:** ✅ Logs flowing to CloudWatch successfully

![IAM Fix](screenshots/iam-permissions-fixed.png)

---

### 5️⃣ GuardDuty Security Findings

**Problem:** GuardDuty detected potential unauthorized access  
**Investigation:**
- Reviewed GuardDuty findings
- Analyzed CloudTrail logs
- Identified compromised access key
- Checked affected resources

**Solution:**
1. Rotated compromised IAM access keys
2. Updated Security Group rules
3. Enabled MFA on root account
4. Configured GuardDuty alerts to SNS

**Result:** ✅ Security posture improved, threat mitigated

![GuardDuty Response](screenshots/guardduty-incident-response.png)

---

## 🚀 Quick Start

### Prerequisites
- AWS Account (Free Tier eligible)
- AWS CLI configured
- Terraform installed
- Python 3.8+

### Deploy Lab Environment

```bash
# Clone the repository
git clone https://github.com/charles-bucher/AWS_Cloud_Support_Sim.git
cd AWS_Cloud_Support_Sim

# Initialize Terraform
terraform init

# Review the infrastructure plan
terraform plan

# Deploy the lab environment
terraform apply -auto-approve

# Run scenario simulations
python3 scripts/simulate_errors.py

# Clean up resources when done
terraform destroy -auto-approve
```

### Example: Testing EC2 Scenario

```bash
# Deploy EC2 instance with misconfigured Security Group
cd iac/
terraform apply -target=aws_instance.test_ec2

# Attempt to SSH (will fail initially)
ssh -i key.pem ec2-user@<public-ip>

# Fix Security Group via Terraform
# Update sg_hardening.tf with correct rules
terraform apply

# Verify connectivity
ssh -i key.pem ec2-user@<public-ip>
# Success! ✅
```

---

## 📁 Project Structure

```
AWS_Cloud_Support_Sim/
├── iac/                      # Infrastructure as Code
│   ├── main.tf              # Core Terraform configuration
│   ├── variables.tf         # Input variables
│   ├── outputs.tf           # Output values
│   ├── s3_security.tf       # S3 bucket configurations
│   └── sg_hardening.tf      # Security Group rules
├── scenarios/                # Lab scenarios and documentation
│   ├── ec2_connectivity.md
│   ├── s3_access_denied.md
│   ├── lambda_timeout.md
│   ├── iam_permissions.md
│   └── guardduty_alerts.md
├── scripts/                  # Automation scripts
│   ├── simulate_errors.py   # Generate test scenarios
│   ├── remediation.py       # Automated fixes
│   └── monitoring_setup.py  # CloudWatch configuration
├── tests/                    # Testing scripts
│   └── validate_fixes.py    # Verify solutions work
├── diagrams/                 # Architecture diagrams
│   └── architecture-overview.png
├── screenshots/              # Scenario documentation
│   ├── ec2-connectivity-fix.png
│   ├── s3-access-denied-resolved.png
│   ├── lambda-timeout-resolved.png
│   ├── iam-permissions-fixed.png
│   └── guardduty-incident-response.png
├── docs/                     # Additional documentation
│   └── troubleshooting-playbook.md
├── README.md                 # This file
├── LICENSE.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
└── SECURITY.md
```

---

## 🛠️ Technologies Used

### Cloud Platform
![AWS](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)

### Infrastructure & Automation
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)

### Monitoring & Logging
![CloudWatch](https://img.shields.io/badge/CloudWatch-FF4F8B?style=for-the-badge&logo=amazon-cloudwatch&logoColor=white)

### Security
![IAM](https://img.shields.io/badge/AWS_IAM-DD344C?style=for-the-badge&logo=amazon-aws&logoColor=white)
![GuardDuty](https://img.shields.io/badge/GuardDuty-DD344C?style=for-the-badge&logo=amazon-aws&logoColor=white)

---

## 📚 Learning Journey

This project represents my hands-on learning path in AWS Cloud Support:

**Completed:**
- ✅ AWS fundamentals (EC2, S3, IAM, Lambda)
- ✅ Infrastructure as Code with Terraform
- ✅ CloudWatch monitoring and log analysis
- ✅ Security best practices (IAM, GuardDuty)
- ✅ Troubleshooting methodology

**In Progress:**
- 🔄 AWS Certified Solutions Architect - Associate prep
- 🔄 Advanced networking (VPC peering, Transit Gateway)
- 🔄 Container services (ECS, EKS)

**Next Steps:**
- 📋 AWS Certified SysOps Administrator - Associate
- 📋 Expand to multi-region architectures
- 📋 Add CI/CD pipeline scenarios

---

## 🎓 Why This Project Matters

**For Hiring Managers:**
This project demonstrates I can:
- Troubleshoot production-like AWS issues independently
- Follow structured incident response processes
- Document technical solutions clearly
- Use Infrastructure as Code for repeatable environments
- Think like a Cloud Support Engineer

**Real-World Application:**
These scenarios mirror actual tickets I would handle in a Cloud Support role:
- Customer reports EC2 connectivity issues → investigate and resolve
- Application throwing S3 errors → analyze logs and fix permissions
- Lambda functions failing → debug and optimize
- Security alerts from GuardDuty → respond and remediate

---

## 📞 Contact

**Charles Bucher**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/charles-bucher-cloud)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Charles-Bucher)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:charles.bucher.cloud@gmail.com)

**Open to opportunities in:**
- AWS Cloud Support Engineer
- Junior SysOps Administrator
- Cloud Operations Engineer
- Technical Support Engineer (Cloud)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

## 🙏 Acknowledgments

- AWS Documentation for best practices
- HashiCorp for Terraform
- The cloud computing community for continuous learning resources

---

<div align="center">

**⭐ If you find this project helpful, please consider giving it a star!**

Made with ☕ and determination by Charles Bucher

</div>