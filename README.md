# AWS Cloud Support Simulator

<div align="center">

![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![CloudWatch](https://img.shields.io/badge/AWS%20CloudWatch-FF4F8B?style=for-the-badge&logo=amazon-aws&logoColor=white)

**Production-Ready AWS Cloud Support Training | Real-World Incident Simulations**

[🚀 Quick Start](#-quick-start) • [📸 Screenshots](#-screenshots) • [🎯 Scenarios](#-incident-scenarios) • [💼 Skills](#-skills-demonstrated)

</div>

---

## 🎯 Overview

**AWS Cloud Support Simulator** is a hands-on training environment that simulates real-world AWS cloud support scenarios. Designed to build production-ready troubleshooting skills through realistic incident response workflows.

**Perfect for**: Entry-level Cloud Support Engineers, Junior SysOps Engineers, CloudOps roles, and DevOps positions requiring AWS troubleshooting expertise.

### What Makes This Different

| Traditional Learning | AWS Cloud Support Sim |
|---------------------|----------------------|
| 📚 Read documentation | 🔥 **Break real AWS systems** |
| 🎥 Watch tutorials | 🔍 **Troubleshoot actual failures** |
| ✏️ Take notes | 📊 **Analyze real CloudWatch logs** |
| 🤔 Memorize commands | 🛠️ **Fix production-style incidents** |

---

## ✨ Features

### 🎭 Realistic Incident Simulations
- **Multi-service failures**: EC2 connectivity, S3 misconfigurations, Lambda timeouts, GuardDuty alerts
- **Production-style tickets**: Triage → Investigate → Resolve → Document
- **Real AWS resources**: Not mocks or emulators—actual cloud infrastructure
- **Automated environment setup**: Terraform provisions broken environments instantly

### 🔍 Hands-On Troubleshooting
- **Log analysis**: CloudWatch Logs, CloudTrail events, VPC Flow Logs
- **Metrics monitoring**: CPU utilization, network traffic, error rates
- **Root cause analysis**: Systematic investigation workflows
- **Resolution validation**: Confirm fixes work before documenting

### 📊 Professional Workflows
- **Incident response procedures**: Follow real cloud support workflows
- **Documentation standards**: Post-mortems, runbooks, KB articles
- **Escalation criteria**: When to escalate vs. resolve independently
- **Customer communication**: Status updates, resolution summaries

### 🛡️ Security-First Approach
- **GuardDuty integration**: Threat detection and response
- **IAM best practices**: Least privilege access, role-based permissions
- **Security group auditing**: Network access validation
- **Compliance checks**: CIS benchmarks, AWS Well-Architected

### 🤖 Automation & Self-Healing
- **Auto-remediation scripts**: Python automation for common issues
- **CloudWatch alarms**: Proactive monitoring and alerting
- **Lambda functions**: Event-driven remediation
- **SNS notifications**: Alert routing and escalation

---

## 🏗️ Architecture

### High-Level Overview

![Architecture Overview](diagrams/architecture-overview-full.svg)



### Component Breakdown

```
AWS Cloud Support Simulator
│
├─── Infrastructure Layer (Terraform)
│    ├── VPC with public/private subnets
│    ├── EC2 instances (web/app/db tiers)
│    ├── S3 buckets (storage & logs)
│    ├── Lambda functions (automation)
│    └── RDS databases (data layer)
│
├─── Monitoring Layer
│    ├── CloudWatch Logs & Metrics
│    ├── CloudWatch Alarms
│    ├── CloudTrail (audit logging)
│    └── GuardDuty (threat detection)
│
├─── Automation Layer
│    ├── Python scripts (boto3)
│    ├── Lambda functions
│    ├── EventBridge rules
│    └── SNS/SQS messaging
│
└─── Incident Scenarios
     ├── EC2 connectivity failures
     ├── S3 security misconfigurations
     ├── Lambda timeout issues
     ├── GuardDuty threat alerts
     ├── High CPU utilization
     ├── DynamoDB throttling
     └── Multi-service outages
```

---

## 🎯 Incident Scenarios

### Available Scenarios

| Scenario | Difficulty | Services | Skills Practiced |
|----------|-----------|----------|------------------|
| EC2 Connectivity Failure | Beginner | EC2, VPC, Security Groups | Network troubleshooting |
| S3 Security Misconfiguration | Beginner | S3, IAM | Security auditing |
| Lambda Timeout Issue | Intermediate | Lambda, CloudWatch | Performance optimization |
| GuardDuty Threat Alert | Intermediate | GuardDuty, IAM | Security incident response |
| High CPU Utilization | Intermediate | EC2, CloudWatch | Performance tuning |
| DynamoDB Throttling | Advanced | DynamoDB, CloudWatch | Database optimization |
| Multi-Service Outage | Advanced | EC2, S3, RDS, VPC | Complex troubleshooting |


---

## 🛠️ Technologies & AWS Services

### AWS Services Used

| Category | Services | Purpose |
|----------|----------|---------|
| **Compute** | EC2, Lambda, Auto Scaling | Application hosting, automation |
| **Storage** | S3, EBS | Object storage, block storage |
| **Database** | RDS, DynamoDB | Relational & NoSQL databases |
| **Networking** | VPC, Security Groups, NACLs, Route53 | Network isolation, access control |
| **Monitoring** | CloudWatch, CloudTrail, X-Ray | Logging, metrics, tracing |
| **Security** | IAM, GuardDuty, Secrets Manager | Identity, threat detection, secrets |
| **Messaging** | SNS, SQS | Notifications, queuing |

### Development Tools

| Tool | Version | Purpose |
|------|---------|---------|
| **Terraform** | 1.0+ | Infrastructure as Code |
| **Python** | 3.8+ | Automation scripts |
| **AWS CLI** | 2.x | Command-line operations |
| **boto3** | Latest | AWS SDK for Python |
| **Git** | 2.x | Version control |

---

## 💼 Skills Demonstrated

### Cloud Operations (CloudOps)
✅ **Infrastructure Management**
- Provisioning AWS resources with Terraform
- Managing EC2 instances, load balancers, auto-scaling
- VPC design and network configuration

✅ **Monitoring & Observability**
- CloudWatch dashboards and alarms
- Log aggregation and analysis
- Metric-based alerting

✅ **Incident Response**
- Triaging production incidents
- Root cause analysis
- Systematic troubleshooting

### System Operations (SysOps)
✅ **System Administration**
- Linux server management
- Process monitoring and debugging
- Resource optimization

✅ **Automation**
- Python scripting with boto3
- Lambda function development
- Event-driven automation

✅ **Performance Tuning**
- CPU/memory optimization
- Database query optimization
- Network performance troubleshooting

### DevOps Practices
✅ **Infrastructure as Code**
- Terraform module development
- Version-controlled infrastructure
- Repeatable deployments

✅ **CI/CD Principles**
- Automated testing
- Deployment pipelines
- Rollback procedures

✅ **Configuration Management**
- Environment standardization
- Credential management
- Secrets rotation

### Cloud Support Skills
✅ **Customer-Facing**
- Technical communication
- Status updates
- Solution documentation

✅ **Problem Solving**
- Analytical thinking
- Debug complex issues
- Pattern recognition

✅ **Documentation**
- Runbook creation
- KB article writing
- Post-mortem reports

---

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have:

- ✅ **AWS Account** (Free Tier eligible)
- ✅ **AWS CLI** configured with credentials
- ✅ **Terraform** >= 1.0 installed
- ✅ **Python** >= 3.8 installed
- ✅ **Git** installed

### Installation

**Step 1: Clone the Repository**

```bash
git clone https://github.com/charles-bucher/AWS_Cloud_Support_Sim.git
cd AWS_Cloud_Support_Sim
```

**Step 2: Configure AWS Credentials**

```bash
aws configure
# Enter your AWS Access Key ID
# Enter your AWS Secret Access Key
# Default region: us-east-1
# Default output format: json
```

**Step 3: Initialize Terraform**

```bash
cd terraform
terraform init
```

**Step 4: Review Terraform Plan**

```bash
terraform plan
# Review resources that will be created
```

**Step 5: Deploy Infrastructure**

```bash
terraform apply
# Type 'yes' to confirm
# Wait 5-10 minutes for resources to provision
```

**Step 6: Verify Deployment**

```bash
# Check AWS Console or use CLI
aws ec2 describe-instances --filters "Name=tag:Project,Values=CloudSupportSim"
aws s3 ls | grep cloud-support-sim
```

### Running a Scenario

**Choose a scenario:**

```bash
cd scenarios/01_ec2-connectivity-failure
```

**Read the scenario description:**

```bash
cat README.md
```

**Follow the troubleshooting workflow:**

1. **Triage**: Gather initial information
2. **Investigate**: Analyze logs and metrics
3. **Diagnose**: Identify root cause
4. **Resolve**: Apply fix
5. **Validate**: Confirm resolution
6. **Document**: Write post-mortem

**Example commands:**

```bash
# View CloudWatch logs
aws logs tail /aws/ec2/instances --follow

# Check EC2 instance status
aws ec2 describe-instance-status --instance-ids i-1234567890abcdef0

# Review security group rules
aws ec2 describe-security-groups --group-ids sg-0123456789abcdef0
```

### Cleanup

**Destroy all resources to avoid AWS charges:**

```bash
cd terraform
terraform destroy
# Type 'yes' to confirm
```

---

## 📸 Screenshots

### Infrastructure Setup

**Lab Environment**

![Lab Environment](screenshots/00_lab_environment_verified.png)

**VPC & Networking**

![VPC Configuration](screenshots/01_vpc_architecture_setup.png)

![VPC Configuration](screenshots/02_vpc_subnets_routing.png)

**Security Configuration**

![Security Setup](screenshots/03_security_groups_network_acls.png)

**IAM Roles & Policies**

![IAM Configuration](screenshots/04_iam_roles_policies_setup.png)

**S3 Storage**

![S3 Configuration](screenshots/06_s3_bucket_setup.png)

![S3 Configuration](screenshots/08_s3_bucket_configuration.png)

**Monitoring & Security**

![Monitoring Setup](screenshots/07_guardduty_dashboard_overview.png)

![Monitoring Setup](screenshots/09_cloudwatch_monitoring_dashboard.png)



---

## 📐 Diagrams

**Architecture Overview Full**

![Architecture Overview Full](diagrams/architecture-overview-full.svg)

**Troubleshooting Workflow**

![Troubleshooting Workflow](diagrams/troubleshooting-workflow.svg)



---

## 📚 Project Structure

```
AWS_Cloud_Support_Sim/
├── README.md                          # This file
├── LICENSE                            # MIT License
├── SECURITY.md                        # Security policy
├── .gitignore                        # Git ignore rules
│
├── terraform/                         # Infrastructure as Code
│   ├── main.tf                       # Main Terraform config
│   ├── variables.tf                  # Input variables
│   ├── outputs.tf                    # Output values
│   ├── modules/                      # Reusable modules
│   │   ├── vpc/                      # VPC module
│   │   ├── ec2/                      # EC2 module
│   │   └── monitoring/               # CloudWatch module
│   └── environments/                 # Environment configs
│       ├── dev/
│       └── prod/
│
├── scenarios/                         # Incident scenarios
│   ├── 01_ec2-connectivity-failure/
│   ├── 02_s3-security-misconfiguration/
│   ├── 03_lambda-timeout-issue/
│   ├── 04_guardduty-threat-alert/
│   ├── 05_high-cpu-utilization/
│   ├── 06_dynamodb-throttling/
│   └── 07_multi-service-outage/
│
├── scripts/                           # Automation scripts
│   ├── setup/                        # Setup scripts
│   ├── monitoring/                   # Monitoring scripts
│   ├── remediation/                  # Auto-fix scripts
│   └── cleanup/                      # Cleanup scripts
│
├── docs/                              # Documentation
│   ├── architecture/                 # Architecture docs
│   ├── runbooks/                     # Operational runbooks
│   ├── postmortems/                  # Incident reports
│   └── guides/                       # How-to guides
│
├── diagrams/                          # Architecture diagrams
│   ├── architecture-overview.svg
│   ├── network-topology.svg
│   └── troubleshooting-workflow.svg
│
└── screenshots/                       # Visual documentation
    ├── 00_lab_environment_verified.png
    ├── 01_vpc_architecture_setup.png
    └── [additional screenshots]
```

---

## 🎓 Learning Path

### For Beginners
1. Start with basic EC2 connectivity issues
2. Learn CloudWatch log analysis
3. Understand VPC networking fundamentals
4. Practice security group troubleshooting

### For Intermediate Users
1. Multi-tier application debugging
2. Lambda function optimization
3. Database performance tuning
4. Security incident response

### For Advanced Users
1. Multi-service failure scenarios
2. Custom automation development
3. Advanced monitoring setups
4. Cost optimization strategies

---

## 🎯 Certification Alignment

### AWS Certified Cloud Practitioner (CLF-C02)
✅ EC2, S3, VPC, IAM fundamentals  
✅ AWS pricing and support models  
✅ Security and compliance basics

### AWS Certified Solutions Architect - Associate (SAA-C03)
✅ Design resilient architectures  
✅ High-performance architectures  
✅ Secure applications and architectures  
✅ Cost-optimized architectures

### AWS Certified SysOps Administrator - Associate (SOA-C02)
✅ Deploy, manage, and operate AWS  
✅ Implement security controls  
✅ Provision and manage AWS resources  
✅ Monitor and report on AWS usage

### AWS Certified DevOps Engineer - Professional (DOP-C02)
✅ Implement CI/CD pipelines  
✅ Configuration management  
✅ Monitoring and logging  
✅ Incident response automation

---

## 🏆 Career Alignment

### Entry-Level Cloud Support Engineer
**What You'll Demonstrate:**
- Customer ticket handling (via incident scenarios)
- Log analysis and troubleshooting
- AWS service knowledge (EC2, S3, Lambda, VPC)
- Documentation skills (runbooks, post-mortems)

**Key Skills Proven:**
- Problem-solving under pressure
- Clear technical communication
- AWS Console proficiency
- Basic automation (Python/boto3)

### Junior SysOps Engineer
**What You'll Demonstrate:**
- Infrastructure monitoring and alerting
- Performance troubleshooting
- Automation scripting
- Security best practices

**Key Skills Proven:**
- CloudWatch expertise
- Terraform infrastructure management
- Linux system administration
- Proactive problem prevention

### CloudOps Engineer
**What You'll Demonstrate:**
- End-to-end cloud operations
- Self-healing infrastructure
- Cost optimization
- Multi-service orchestration

**Key Skills Proven:**
- Infrastructure as Code (Terraform)
- Event-driven automation (Lambda)
- Observability (logs, metrics, traces)
- Incident response procedures

### Junior DevOps Engineer
**What You'll Demonstrate:**
- Infrastructure automation
- CI/CD principles
- Configuration management
- Deployment strategies

**Key Skills Proven:**
- Git version control
- Python automation
- AWS API usage (boto3)
- Collaboration workflows

---

## 💡 Tips for Using This Portfolio

### For Job Applications
1. **Link this repo** in your resume under "Projects"
2. **Reference specific scenarios** in cover letters
3. **Discuss incidents** during technical interviews
4. **Show runbooks** as documentation examples

### For Technical Interviews
1. **Walk through a scenario** step-by-step
2. **Explain your troubleshooting process**
3. **Discuss lessons learned**
4. **Demonstrate AWS CLI commands**

### For Recruiters/Hiring Managers
This repository demonstrates:
- ✅ Hands-on AWS experience (not just theory)
- ✅ Production troubleshooting skills
- ✅ Documentation abilities
- ✅ Self-directed learning
- ✅ Professional workflows

---

## 🔒 Security

See [SECURITY.md](SECURITY.md) for security policies and vulnerability reporting.

**Security Features:**
- ✅ No hardcoded credentials
- ✅ IAM least privilege access
- ✅ GuardDuty threat detection
- ✅ CloudTrail audit logging
- ✅ Security group restrictive rules

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Charles Bucher**  
*AWS Cloud Support & CloudOps Engineer*

Demonstrating production-ready cloud operations skills through hands-on incident simulations.

### 📫 Connect With Me

<div align="center">

[![Portfolio](https://img.shields.io/badge/Portfolio-charles--bucher.github.io-blue?style=for-the-badge&logo=github)](https://charles-bucher.github.io)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-charles--bucher--cloud-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/charles-bucher-cloud)
[![GitHub](https://img.shields.io/badge/GitHub-charles--bucher-181717?style=for-the-badge&logo=github)](https://github.com/charles-bucher)
[![Email](https://img.shields.io/badge/Email-quietopscb%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:quietopscb@gmail.com)

</div>

### 🚀 Other Projects

- [**AWS Error-Driven Troubleshooting Lab**](https://github.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab) - Intentionally broken AWS scenarios
- [**CloudOpsLab**](https://github.com/charles-bucher/CloudOpsLab) - Monitoring and self-healing automation
- [**AWS Cost Optimizer**](https://github.com/charles-bucher/AWS-Cost-Optimization-Tool-) - Automated cost analysis tool

---

## 🙏 Acknowledgments

- AWS Documentation and best practices
- Cloud community resources
- Open source tools and libraries
- Fellow cloud engineers sharing knowledge

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Built with ☁️ by Charles Bucher

*Making cloud support skills tangible through hands-on practice*

</div>
