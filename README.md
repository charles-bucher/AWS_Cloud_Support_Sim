# AWS Cloud Support Simulation 🛠️☁️

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![AWS](https://img.shields.io/badge/AWS-Cloud%20Support-FF9900?logo=amazon-aws)](https://aws.amazon.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Terraform](https://img.shields.io/badge/Terraform-IaC-7B42BC?logo=terraform)](https://www.terraform.io/)

## 🚀 Project Overview

Hands-on AWS Cloud Support lab simulating real-world troubleshooting scenarios. Built while self-teaching cloud technologies to demonstrate practical skills for Cloud Support Engineer and Technical Support roles.

**What's Included:**
- ✅ **8 troubleshooting scenarios** with screenshot documentation
- ✅ **AWS services**: EC2, VPC, S3, IAM, Lambda, GuardDuty, CloudFormation
- ✅ **Python automation** using Boto3 SDK
- ✅ **Infrastructure as Code** with Terraform
- ✅ **Git workflows** for version control
- ✅ **Professional documentation** with visual evidence

**Target Roles:** Cloud Support Engineer • Technical Support Engineer • CloudOps • IT Support Specialist • Junior DevOps

---

## 📊 Project Screenshots

<table>
<tr>
<td width="50%">

![VPC Setup](screenshots/ACSS_01_VPC_Setup.png)
**VPC Network Setup**
- VPC architecture design
- Internet gateway configuration
- Network planning

</td>
<td width="50%">

![Subnets & Routes](screenshots/ACSS_02_Subnets_RouteTables.png)
**Subnets & Route Tables**
- Public/private subnet configuration
- Route table associations
- Traffic routing

</td>
</tr>
<tr>
<td width="50%">

![Security Groups](screenshots/ACSS_03_SecurityGroups_NACLs.png)
**Security Groups & NACLs**
- Security rule configuration
- Access control troubleshooting
- Network security

</td>
<td width="50%">

![Git Workflow](screenshots/ACSS_04_Git-Branch-Merge-Workflow.png)
**Git Version Control**
- Branch-merge workflow
- Infrastructure code versioning
- Collaboration practices

</td>
</tr>
<tr>
<td width="50%">

![GuardDuty Automation](screenshots/ACSS_05_Python-Boto3-GuardDuty-Findings-Automation.png)
**Security Automation**
- Python/Boto3 scripts
- GuardDuty integration
- Automated responses

</td>
<td width="50%">

![S3 Buckets](screenshots/ACSS_06_S3_Buckets.png)
**S3 Storage Management**
- Bucket configuration
- Permission troubleshooting
- Access policies

</td>
</tr>
<tr>
<td width="50%">

![IAM Configuration](screenshots/ACSS_07_IAM_Roles_Policies.png)
**IAM Roles & Policies**
- Identity management
- Permission configuration
- Access troubleshooting

</td>
<td width="50%">

![Service Health](screenshots/ACSS_08_Service_Health.png)
**CloudWatch Monitoring**
- Service health checks
- Metrics and alarms
- Monitoring dashboards

</td>
</tr>
</table>

---

## 🎯 Skills & Technologies

| **Category** | **Technologies** |
|---|---|
| **Cloud Platform** | AWS (EC2, VPC, S3, IAM, Lambda, GuardDuty, CloudFormation) |
| **Networking** | VPC, Subnets, Route Tables, Security Groups, NACLs, Internet Gateway |
| **Infrastructure as Code** | Terraform, CloudFormation, YAML, HCL |
| **Scripting & Automation** | Python 3.8+, Boto3 SDK, AWS CLI |
| **Monitoring & Logging** | CloudWatch (metrics, alarms, logs) |
| **Version Control** | Git, GitHub |
| **Security** | IAM policies, Security Groups, GuardDuty, encryption |
| **Problem Solving** | Troubleshooting, root cause analysis, documentation |

**Keywords for Job Search:** AWS Cloud Support, Technical Support Engineer, Cloud Operations, EC2, VPC, Security Groups, CloudFormation, Terraform, S3, IAM, Python, Boto3, Network Troubleshooting, Infrastructure as Code, GuardDuty, CloudWatch, DevOps, IT Support, NOC, System Administration, Monitoring, Automation

---

## 📂 Repository Structure

```
AWS_Cloud_Support_Sim/
├── screenshots/           # Visual documentation
├── scenarios/            # CloudFormation templates & guides
├── scripts/              # Python automation scripts
├── main.py              # Primary simulation script
├── main.tf              # Terraform configuration
├── utils.py             # Helper functions
└── requirements.txt     # Python dependencies
```

---

## ⚡ Quick Start

```bash
# Clone repository
git clone https://github.com/charles-bucher/AWS_Cloud_Support_Sim.git
cd AWS_Cloud_Support_Sim

# Create virtual environment
python -m venv venv

# Activate environment (Windows)
.\venv\Scripts\activate

# Activate environment (Linux/Mac)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure AWS CLI
aws configure

# Run simulation
python main.py
```

---

## 🏗️ Troubleshooting Scenarios

### 1. VPC Network Architecture
- Design VPC with proper CIDR blocks
- Configure internet gateway
- Set up network connectivity
- [Screenshot](screenshots/ACSS_01_VPC_Setup.png)

### 2. Subnet & Route Configuration
- Create public and private subnets
- Configure route tables
- Troubleshoot routing issues
- [Screenshot](screenshots/ACSS_02_Subnets_RouteTables.png)

### 3. Security Groups & Network ACLs
- Configure security group rules
- Set up network ACLs
- Fix connectivity problems
- Validate security configurations
- [Screenshot](screenshots/ACSS_03_SecurityGroups_NACLs.png)

### 4. Git Version Control Workflow
- Implement branching strategy
- Manage infrastructure code versions
- Handle merge workflows
- [Screenshot](screenshots/ACSS_04_Git-Branch-Merge-Workflow.png)

### 5. GuardDuty Security Automation
- Automate security finding detection
- Build Python/Boto3 remediation scripts
- Integrate with CloudWatch
- [Screenshot](screenshots/ACSS_05_Python-Boto3-GuardDuty-Findings-Automation.png)

### 6. S3 Bucket Management
- Configure bucket policies
- Troubleshoot access denied errors
- Implement proper permissions
- [Screenshot](screenshots/ACSS_06_S3_Buckets.png)

### 7. IAM Roles & Policies
- Create and attach IAM policies
- Troubleshoot permission issues
- Implement least-privilege access
- [Screenshot](screenshots/ACSS_07_IAM_Roles_Policies.png)

### 8. CloudWatch Monitoring
- Set up metrics and alarms
- Monitor service health
- Create dashboards
- [Screenshot](screenshots/ACSS_08_Service_Health.png)

---

## 📝 What I Learned

**AWS Services:** Hands-on experience with EC2, VPC, Security Groups, S3, Lambda, GuardDuty, CloudFormation, IAM, and CloudWatch.

**Troubleshooting:** Network connectivity issues, permission problems, security configurations, and infrastructure deployment errors.

**Automation:** Writing Python scripts with Boto3 to interact with AWS services, automate monitoring, and respond to security findings.

**Infrastructure as Code:** Using Terraform and CloudFormation to define and deploy infrastructure programmatically.

**DevOps Practices:** Git workflows, version control, documentation, and systematic problem-solving approaches.

---

## 🎯 Next Steps

- [ ] Add RDS connectivity troubleshooting
- [ ] Lambda error handling scenarios
- [ ] VPC Peering configuration
- [ ] ELB health check troubleshooting
- [ ] Auto Scaling scenarios
- [ ] Cost optimization examples

---

## 🤝 Contributing

Contributions welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

## 🔐 Security

Please review [SECURITY.md](SECURITY.md) for reporting vulnerabilities.

---

## 📧 Contact

**Charles Bucher**  
📍 Pinellas Park, Florida  
✉️ quietopscb@gmail.com

🔗 [GitHub](https://github.com/charles-bucher) • [LinkedIn](https://linkedin.com/in/charles-bucher-cloud)

---

## 📚 Resources

- [AWS Documentation](https://docs.aws.amazon.com/)
- [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [AWS Skill Builder](https://skillbuilder.aws/) - Free AWS training

---

**⭐ If you find this project helpful, please consider giving it a star!**

---

<div align="center">

**Self-taught AWS Cloud Support portfolio project**

*Demonstrating practical cloud troubleshooting skills*

</div>