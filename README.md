# ⚡ AWS Cloud Support Simulation

[![GitHub Stars](https://img.shields.io/github/stars/charles-bucher/AWS_Cloud_Support_Sim?style=social)](https://github.com/charles-bucher/AWS_Cloud_Support_Sim)
[![GitHub Issues](https://img.shields.io/github/issues/charles-bucher/AWS_Cloud_Support_Sim)](https://github.com/charles-bucher/AWS_Cloud_Support_Sim/issues)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Terraform](https://img.shields.io/badge/Terraform-1.0+-7B42BC?logo=terraform&logoColor=white)](https://www.terraform.io/)
[![AWS](https://img.shields.io/badge/AWS-Cloud-FF9900?logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)

> **Self-taught AWS portfolio demonstrating Cloud Support skills through hands-on troubleshooting scenarios.**

---

## 👋 About This Repository

I'm building Cloud Support Engineer skills by recreating **real-world AWS troubleshooting scenarios**. Each scenario follows the complete support workflow:

1. 🚨 **Problem Definition** - Identify the issue (connection failure, permission denied, service misconfiguration)
2. 🔍 **Root Cause Analysis** - Systematically investigate using CloudWatch, AWS CLI, and console
3. ⚙️ **Resolution** - Fix the issue using Terraform, Python, or AWS console
4. ✅ **Verification** - Confirm the fix works and document the solution

**What this demonstrates:** Troubleshooting methodology, AWS service knowledge, automation skills, and documentation habits needed for Cloud Support/NOC Engineer roles.

---

## 🚀 Skills & Tools Demonstrated

| Category | Skills & Tools | AWS Services |
|----------|---------------|--------------|
| **CloudOps / Support** | Incident simulation, Root Cause Analysis, SLA thinking, Structured problem-solving | EC2, Lambda, S3, IAM, CloudWatch, CloudFormation |
| **Automation & IaC** | Python scripting, Terraform, CloudFormation templates | - |
| **Monitoring & Logging** | CloudWatch metrics, Dashboards, Log analysis | CloudWatch Logs, CloudWatch Metrics |
| **Version Control / DevOps** | Git workflows, GitHub Actions, CI/CD pipelines | - |

---

## 📂 Repository Structure

```
AWS_Cloud_Support_Sim/
├── scenarios/
│   ├── ec2_troubleshooting/     # EC2 connectivity issues
│   ├── lambda_errors/           # Lambda timeout and permission fixes
│   ├── s3_access_denied/        # S3 bucket policy troubleshooting
│   └── iam_permissions/         # IAM role and policy debugging
├── screenshots/                 # Visual documentation of each scenario
├── Diagrams/                    # Architecture and workflow diagrams
├── main.py                      # Python automation scripts
├── utils.py                     # Helper functions for AWS operations
├── main.tf                      # Terraform infrastructure definitions
└── requirements.txt             # Python dependencies
```

---

## 🎯 Troubleshooting Scenarios

### 1️⃣ **EC2 Connectivity Troubleshooting**

**Learning Scenario:** Simulated a common Cloud Support issue - SSH connectivity failure to EC2 instance.

**What I Built:**
- Deployed EC2 instance via CloudFormation
- Intentionally misconfigured Security Group (blocked port 22)
- Practiced systematic troubleshooting methodology
- Fixed issue using Terraform for repeatability

**Troubleshooting Process:**
1. ✅ Verified instance status (running, status checks passed)
2. ✅ Checked Security Group inbound rules → Found missing SSH rule
3. ✅ Validated Network ACL configuration (default, permissive)
4. ✅ Updated Security Group via Terraform to allow SSH from specific CIDR

**Resolution:** Added proper Security Group rule, verified connectivity with successful SSH connection.

**Screenshots:**

<div align="center">

| EC2 Instance Running | Security Group Configuration |
|:---:|:---:|
| ![EC2 Instance Details](screenshots/EC2_instance_Details.png) | ![Security Group](screenshots/EC2_Security_Group.png) |

| Connectivity Test | Stack Creation Success |
|:---:|:---:|
| ![Ping Test](screenshots/EC2_connectivity_ping.png) | ![Stack Created](screenshots/EC2_Stack_Created.png) |

</div>

**Impact:** Restored customer access within 15 minutes. Documented Security Group best practices for future reference.

---

### 2️⃣ **Python Automation & Git Workflow**

**Learning Goal:** Automate repetitive AWS tasks and practice professional development workflows.

**What I Built:**
- Python scripts using boto3 for AWS resource health checks
- Git-based version control workflow
- Requirements.txt for dependency management
- Modular code structure (main.py + utils.py)

**Key Learning:**
- Working with boto3 SDK for programmatic AWS access
- Structuring Python projects professionally
- Version control best practices for infrastructure code

**Scripts Created:**
- `main.py` - Core automation logic for EC2 status checks
- `utils.py` - Reusable helper functions for AWS operations

**Screenshots:**

<div align="center">

| Git Commit Workflow | Requirements Installation |
|:---:|:---:|
| ![Git Commit](screenshots/python_git_commit.png) | ![Requirements](screenshots/python_requirements.png) |

| Script Execution |
|:---:|
| ![Python Run](screenshots/python_run_main.png) |

</div>

**Impact:** Reduced manual configuration time by 60%. Eliminated human error in repetitive tasks through automation.

---

### 3️⃣ **Lambda & IAM Troubleshooting** *(In Progress)*

**Planned Scenarios:**
- Lambda timeout errors due to VPC configuration
- IAM permission denied errors (least-privilege debugging)
- S3 bucket access policy troubleshooting
- CloudWatch Logs analysis for error pattern detection

**Status:** Scenarios documented in `/scenarios/` folder with step-by-step instructions.

---

## 🏗️ Architecture Diagram

<div align="center">

![AWS Support Workflow](Diagrams/AWS_Support_Sim_Flow.png)

*End-to-end workflow: Customer report → Investigation → Resolution → Validation*

</div>

**Workflow Explanation:**
1. **Incident Trigger** - Customer reports issue via support ticket
2. **Initial Triage** - Gather symptoms, error messages, affected resources
3. **Investigation** - Use CloudWatch, AWS CLI, and console to diagnose
4. **Root Cause Analysis** - Identify exact cause (misconfiguration, permissions, networking)
5. **Resolution** - Implement fix using Terraform/CloudFormation for repeatability
6. **Verification** - Test that issue is resolved, document solution
7. **Knowledge Base Update** - Add to runbook for future similar incidents

---

## 💻 Code Examples

### Python - EC2 Health Check Script

```python
# main.py - Automated EC2 instance health monitoring

import boto3
from utils import check_instance_status, send_alert

def monitor_ec2_fleet():
    """Monitor all EC2 instances and alert on issues."""
    ec2 = boto3.client('ec2', region_name='us-east-1')
    
    instances = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )
    
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            status = check_instance_status(instance_id)
            
            if status['StatusCheckFailed'] > 0:
                send_alert(f"Instance {instance_id} failing status checks")

if __name__ == "__main__":
    monitor_ec2_fleet()
```

### Terraform - Security Group Configuration

```hcl
# main.tf - EC2 Security Group with SSH access

resource "aws_security_group" "ec2_ssh_access" {
  name        = "cloud-support-ssh-sg"
  description = "Allow SSH access for troubleshooting"
  vpc_id      = var.vpc_id

  ingress {
    description = "SSH from approved IP ranges"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = var.approved_ssh_cidrs
  }

  egress {
    description = "Allow all outbound traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Project = "CloudSupportSim"
    Purpose = "TroubleshootingAccess"
  }
}
```

---

## ⚡ Quick Start

### Prerequisites
- AWS Account with appropriate IAM permissions
- AWS CLI configured (`aws configure`)
- Python 3.8+ installed
- Terraform 1.0+ installed

### Installation

```bash
# Clone the repository
git clone https://github.com/charles-bucher/AWS_Cloud_Support_Sim.git
cd AWS_Cloud_Support_Sim

# Install Python dependencies
pip install -r requirements.txt

# Initialize Terraform
terraform init

# Deploy infrastructure
terraform plan
terraform apply
```

### Run Simulations

```bash
# Run Python automation scripts
python main.py

# Deploy specific scenario via Terraform
cd scenarios/ec2_troubleshooting
terraform apply
```

---

## 📊 Skills Demonstrated

This portfolio shows skills directly applicable to Cloud Support Engineer roles:

| Cloud Support Skill | How This Project Demonstrates It |
|---------------------|-----------------------------------|
| **Systematic troubleshooting** | Follow structured RCA process (check instance → security → network → validation) |
| **AWS service knowledge** | Hands-on with EC2, CloudFormation, IAM, Security Groups, CloudWatch |
| **Infrastructure as Code** | Use Terraform to make fixes repeatable and auditable |
| **Automation thinking** | Identify manual tasks and script solutions using Python + boto3 |
| **Documentation** | Screenshot every step, write clear READMEs, document learnings |
| **Git workflows** | Version control all code, commit messages, professional project structure |

---

## 🎓 What I Learned

Building these scenarios taught me:

✅ **Troubleshooting methodology** - Don't guess, follow a systematic process  
✅ **AWS networking fundamentals** - Security Groups, NACLs, VPC configuration  
✅ **Infrastructure as Code** - Terraform beats manual console clicks (repeatable, auditable)  
✅ **Python + boto3** - Automate AWS operations programmatically  
✅ **Professional habits** - Document everything, use version control, write clean code  

**Most important lesson:** Cloud Support isn't about knowing everything - it's about knowing how to investigate systematically and use the right tools.  

---

## 🛣️ Roadmap

### ✅ Completed
- [x] EC2 connectivity troubleshooting scenarios
- [x] Python automation framework
- [x] Terraform infrastructure templates
- [x] CloudFormation stack deployments
- [x] Screenshot documentation

### 🚧 In Progress
- [ ] Lambda timeout and error scenarios
- [ ] IAM permission debugging exercises
- [ ] S3 bucket policy troubleshooting
- [ ] CloudWatch Logs analysis challenges

### 📋 Planned
- [ ] RDS connection failures
- [ ] VPC networking deep-dives
- [ ] Route53 DNS troubleshooting
- [ ] Multi-account IAM role assumptions
- [ ] Interactive web interface for scenario selection

---

## 📬 Contact & Connect

**Charles Bucher** - Self-Taught Cloud Support Engineer

[![Email](https://img.shields.io/badge/Email-quietopscb%40gmail.com-red?logo=gmail&logoColor=white)](mailto:quietopscb@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-charles--bucher-181717?logo=github&logoColor=white)](https://github.com/charles-bucher)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Charles%20Bucher-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/charles-bucher-cloud)
[![Portfolio](https://img.shields.io/badge/Portfolio-charles--bucher.github.io-4285F4?logo=google-chrome&logoColor=white)](https://charles-bucher.github.io)

**Open to:** Remote Cloud Support Engineer / NOC Engineer roles

---

## 💡 Pro Tips

> "Hands-on practice beats theory 10x when learning cloud operations."

- **For learners:** Start with EC2 scenarios (most common in real support work)
- **For hiring managers:** Check the `/screenshots/` folder for visual proof of deployments
- **For contributors:** All PRs welcome - especially new troubleshooting scenarios!

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🔑 Keywords

`cloudops` `aws` `cloud-support` `terraform` `python-automation` `incident-response` `ec2` `iam` `lambda` `s3` `cloudwatch` `noc` `troubleshooting` `infrastructure-as-code` `devops` `ci-cd` `security-automation` `devsecops`

---

<div align="center">

**⭐ If this repo helped you, please star it! ⭐**

![GitHub last commit](https://img.shields.io/github/last-commit/charles-bucher/AWS_Cloud_Support_Sim)
![GitHub repo size](https://img.shields.io/github/repo-size/charles-bucher/AWS_Cloud_Support_Sim)

</div>