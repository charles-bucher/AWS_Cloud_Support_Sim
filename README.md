# AWS Cloud Support Simulator 🚀

![AWS](https://img.shields.io/badge/AWS-Cloud_Support-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Python](https://img.shields.io/badge/Python-Automation-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-IaC-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

[![Self-Study](https://img.shields.io/badge/Self--Study-Learning-blue?style=flat-square)](https://github.com/charles-bucher)
[![Open to Work](https://img.shields.io/badge/Open_to_Work-Yes-brightgreen?style=flat-square)](https://linkedin.com/in/charles-bucher-cloud)

**Hands-on AWS Cloud Support experience through real-world troubleshooting scenarios**

*Self-taught cloud engineer building skills through systematic problem-solving and professional documentation*

---

## 📑 Table of Contents

- [About This Project](#about-this-project)
- [My Learning Journey](#my-learning-journey)
- [Architecture](#architecture)
- [Lab Scenarios](#lab-scenarios)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Technologies](#technologies)
- [What I'm Learning](#what-im-learning)
- [Career Goals](#career-goals)
- [Contact](#contact)

---

## 🎯 About This Project

### The Short Answer
I'm building proof of AWS cloud support skills through hands-on practice—not just watching tutorials.

### The Real Story
I'm transitioning from delivery work to cloud operations. I have a felony record from 2003 (clean since 2008, now 40 with three kids). I know I need to **work twice as hard** to get an interview.

Instead of asking for chances, **I'm creating proof**:
- ✅ Real AWS infrastructure I deployed (my account, my money)
- ✅ Real problems I broke intentionally and fixed systematically
- ✅ Real documentation showing how I troubleshoot
- ✅ Real screenshots proving I did the work

**This isn't theory. This is my actual learning lab running on AWS.**

---

## 🎓 My Learning Journey

### Background (Honest Status)
- **Current:** Self-teaching AWS while working part-time delivery
- **Goal:** Entry-level AWS Cloud Support or SysOps Administrator role
- **Location:** Florida (remote preferred)
- **Timeline:** Started December 2024, actively learning January 2025

### ✅ Completed (Verified)

```
Infrastructure Deployed:
├─ Custom VPC with public/private subnets
├─ EC2 instances with proper security groups
├─ S3 buckets with IAM policies
├─ Lambda functions with CloudWatch integration
└─ GuardDuty threat detection enabled

Skills Practiced:
├─ 5 real troubleshooting scenarios documented
├─ CloudWatch Logs analysis and metric interpretation
├─ IAM policy debugging and permission troubleshooting
├─ Terraform for Infrastructure as Code
└─ Professional documentation (runbooks, RCAs)
```

### 🔄 Currently Working On

- AWS Solutions Architect Associate certification prep
- Adding Auto Scaling Groups and Load Balancer scenarios
- Learning CloudFormation alongside Terraform
- Building CI/CD pipeline understanding

### 📋 Planned Next

- Take AWS SAA exam (when ready, no date yet)
- Container basics with ECS
- Advanced monitoring and alerting scenarios
- Cost optimization practices

---

## 💻 Skills I've Built (No Exaggeration)

| Skill | Level | Evidence |
|-------|-------|----------|
| **AWS Console Navigation** | Comfortable | [Screenshots throughout repo](screenshots/) |
| **EC2 Troubleshooting** | Learning | [Scenario 1](scenarios/ec2_connectivity.md) |
| **S3 Operations** | Learning | [Scenario 2](scenarios/s3_access_denied.md) |
| **IAM Policy Debugging** | Basic | [Scenario 4](scenarios/iam_permissions.md) |
| **CloudWatch Logs** | Basic | All scenarios use log analysis |
| **Lambda Functions** | Learning | [Scenario 3](scenarios/lambda_timeout.md) |
| **Terraform** | Beginner | [All infrastructure](iac/) |
| **Python Scripting** | Basic | [Automation scripts](scripts/) |
| **Linux/Bash** | Comfortable | Daily use for lab work |
| **Git/GitHub** | Comfortable | This repo proves it |
| **Documentation** | Strong | Professional runbooks created |

**Translation for employers:** I'm entry-level, but I can prove I've actually built things in AWS and can troubleshoot systematically.

---

## 🏗️ Architecture

### Lab Environment Overview

![Lab Environment](https://raw.githubusercontent.com/charles-bucher/AWS_Cloud_Support_Sim/main/diagrams/lab-environment.png)

*Complete lab environment deployed via Terraform showing VPC, compute, security, and monitoring components*

### VPC Architecture

![VPC Architecture](https://raw.githubusercontent.com/charles-bucher/AWS_Cloud_Support_Sim/main/diagrams/vpc-architecture.png)

*Production-ready VPC with public/private subnets, NAT gateway, route tables, and security groups*

### Components Deployed

```
┌──────────────────────────────────────────────────────────────┐
│                      AWS Cloud (us-east-1)                   │
│                                                              │
│  ┌─────────────────┐        ┌─────────────────┐            │
│  │      VPC        │        │   CloudWatch    │            │
│  │  10.0.0.0/16    │        │                 │            │
│  │                 │        │  ├─ Logs        │            │
│  │  ┌───────────┐  │───────▶│  ├─ Metrics    │            │
│  │  │    EC2    │  │        │  └─ Alarms     │            │
│  │  │ Instance  │  │        │                 │            │
│  │  └───────────┘  │        └─────────────────┘            │
│  │                 │                                        │
│  │  ┌───────────┐  │        ┌─────────────────┐            │
│  │  │    S3     │  │        │   GuardDuty     │            │
│  │  │  Bucket   │  │        │                 │            │
│  │  └───────────┘  │        │  ├─ Findings    │            │
│  │                 │        │  └─ Alerts      │            │
│  │  ┌───────────┐  │        │                 │            │
│  │  │  Lambda   │  │        └─────────────────┘            │
│  │  │ Function  │  │                                        │
│  │  └───────────┘  │        ┌─────────────────┐            │
│  │                 │        │      IAM        │            │
│  │  ┌───────────┐  │        │                 │            │
│  │  │ Security  │  │───────▶│  ├─ Roles       │            │
│  │  │  Groups   │  │        │  └─ Policies    │            │
│  │  └───────────┘  │        │                 │            │
│  │                 │        └─────────────────┘            │
│  └─────────────────┘                                        │
│                                                              │
│  All deployed via Terraform - Infrastructure as Code        │
└──────────────────────────────────────────────────────────────┘
```

### Incident Response Workflow

```
┌─────────────┐      ┌───────────────┐      ┌──────────────┐      ┌──────────────┐
│   Alert     │─────▶│ Investigation │─────▶│  Root Cause  │─────▶│ Remediation  │
│  Received   │      │   & Logs      │      │   Analysis   │      │  & Testing   │
└─────────────┘      └───────────────┘      └──────────────┘      └──────────────┘
                            │                      │                     │
                            ▼                      ▼                     ▼
                     CloudWatch Logs        IAM Policy Issue      Updated Policy
                     Error Messages         Missing Permissions   Function Success
```

---

## 🔧 Lab Scenarios

### Overview

Each scenario represents a **real problem I created, investigated, and fixed**. This is hands-on learning, not theory.

| Scenario | Services | Skills Practiced | Status |
|----------|----------|------------------|--------|
| [EC2 Connectivity](#1-ec2-connectivity-issues) | EC2, VPC, Security Groups | Network troubleshooting | ✅ Complete |
| [S3 Access Denied](#2-s3-access-denied-errors) | S3, IAM, EC2 | Permission debugging | ✅ Complete |
| [Lambda Timeout](#3-lambda-function-timeout) | Lambda, CloudWatch | Performance optimization | ✅ Complete |
| [IAM Permissions](#4-iam-permission-errors) | IAM, CloudWatch Logs | Policy troubleshooting | ✅ Complete |
| [GuardDuty Alerts](#5-guardduty-security-findings) | GuardDuty, CloudTrail, IAM | Incident response | ✅ Complete |

---

### 1️⃣ EC2 Connectivity Issues

**What I Learned:** SSH troubleshooting and security group configuration

![Security Groups](https://raw.githubusercontent.com/charles-bucher/AWS_Cloud_Support_Sim/main/screenshots/ec2-security-groups.png)

#### Problem I Created
Launched EC2 instance without proper Security Group rules—couldn't SSH in.

#### Investigation Process
```bash
# 1. Checked instance state
aws ec2 describe-instances --instance-ids i-xxxx

# 2. Verified security group rules
aws ec2 describe-security-groups --group-ids sg-xxxx

# 3. Checked route table configuration
aws ec2 describe-route-tables --filters "Name=vpc-id,Values=vpc-xxxx"

# 4. Reviewed VPC Flow Logs
aws ec2 describe-flow-logs
```

#### Root Cause
Security Group missing inbound rule for SSH (port 22)

#### How I Fixed It
```bash
# Added inbound rule for SSH from my IP only (security best practice)
aws ec2 authorize-security-group-ingress \
  --group-id sg-xxxx \
  --protocol tcp \
  --port 22 \
  --cidr MY_IP/32
```

#### Before → After

| Metric | Before | After |
|--------|--------|-------|
| **Security Group** | No port 22 rule | Port 22 from my IP only |
| **Connection** | `ssh: connect to host timeout` | ✅ Successfully authenticated |
| **Resolution Time** | N/A | 12 minutes |

**Key Learning:** Always check Security Groups FIRST when troubleshooting connectivity. Saves hours.

[**Full Walkthrough →**](scenarios/ec2_connectivity.md)

---

### 2️⃣ S3 Access Denied Errors

**What I Learned:** IAM policies control S3 access (not just bucket policies)

![S3 Configuration](https://raw.githubusercontent.com/charles-bucher/AWS_Cloud_Support_Sim/main/screenshots/s3-bucket-config.png)

#### Problem I Created
EC2 instance with application couldn't read/write to S3 bucket despite bucket policy allowing it.

#### Investigation Process
```bash
# 1. Checked S3 bucket policy
aws s3api get-bucket-policy --bucket my-bucket

# 2. Checked IAM role attached to EC2
aws iam get-role --role-name ec2-app-role

# 3. Listed attached policies
aws iam list-attached-role-policies --role-name ec2-app-role

# 4. Analyzed CloudWatch application logs
aws logs tail /aws/ec2/app-logs --follow
```

#### Root Cause
IAM role attached to EC2 instance was missing S3 permissions. Bucket policy alone wasn't enough.

#### How I Fixed It
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "s3:GetObject",
      "s3:PutObject",
      "s3:ListBucket"
    ],
    "Resource": [
      "arn:aws:s3:::my-bucket",
      "arn:aws:s3:::my-bucket/*"
    ]
  }]
}
```

#### Before → After

| Metric | Before | After |
|--------|--------|-------|
| **IAM Policy** | No S3 permissions | Full GetObject/PutObject access |
| **Application** | AccessDenied (403) | ✅ Objects retrieved (200 OK) |
| **Error Rate** | 100% failures | 0% errors |

**Key Learning:** IAM permissions matter! Resource policies (bucket policy) + Identity policies (IAM role) both required.

[**Full Walkthrough →**](scenarios/s3_access_denied.md)

---

### 3️⃣ Lambda Function Timeout

**What I Learned:** Lambda has limits and needs proper configuration

![CloudWatch Dashboard](https://raw.githubusercontent.com/charles-bucher/AWS_Cloud_Support_Sim/main/screenshots/cloudwatch-lambda-metrics.png)

#### Problem I Created
Lambda function timing out at default 3-second limit while processing data.

#### Investigation Process
```bash
# 1. Checked CloudWatch Logs for errors
aws logs tail /aws/lambda/my-function --follow

# 2. Analyzed execution duration metrics
aws cloudwatch get-metric-statistics \
  --namespace AWS/Lambda \
  --metric-name Duration \
  --dimensions Name=FunctionName,Value=my-function \
  --start-time 2025-01-01T00:00:00Z \
  --end-time 2025-01-06T00:00:00Z \
  --period 3600 \
  --statistics Average,Maximum

# 3. Reviewed function configuration
aws lambda get-function-configuration --function-name my-function
```

#### Root Cause
- Default 3-second timeout too low for data processing
- Inefficient code making serial API calls
- No connection pooling

#### How I Fixed It
```python
# Increased timeout configuration
Timeout: 30 seconds (from 3)
Memory: 512 MB (from 128 MB)

# Optimized code
# BEFORE: Serial processing (slow)
for item in items:
    process(item)  # 45 seconds total

# AFTER: Batch processing (fast)
import concurrent.futures
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(process, items)  # 4.2 seconds total
```

#### Before → After

| Metric | Before | After |
|--------|--------|-------|
| **Timeout Setting** | 3 seconds (default) | 30 seconds |
| **Execution Duration** | 3000ms (timeout) | 4200ms (success) |
| **Error Rate** | 95% timeout errors | 0% errors |
| **Performance Improvement** | Baseline | 90% faster |

**Key Learning:** CloudWatch Logs are your best friend. Always check logs first—they tell you exactly what's wrong.

[**Full Walkthrough →**](scenarios/lambda_timeout.md)

---

### 4️⃣ IAM Permission Errors

**What I Learned:** IAM policy syntax matters (ARNs, actions, resources)

![IAM Roles](https://raw.githubusercontent.com/charles-bucher/AWS_Cloud_Support_Sim/main/screenshots/iam-role-policies.png)

#### Problem I Created
Lambda function couldn't write logs to CloudWatch despite having execution role.

#### Investigation Process
```bash
# 1. Checked Lambda execution role
aws lambda get-function-configuration --function-name my-function \
  --query 'Role'

# 2. Listed IAM policies attached to role
aws iam list-attached-role-policies --role-name lambda-execution-role

# 3. Examined policy document
aws iam get-policy-version \
  --policy-arn arn:aws:iam::aws:policy/xxx \
  --version-id v1

# 4. Used IAM Policy Simulator
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::ACCOUNT:role/lambda-execution-role \
  --action-names logs:CreateLogGroup logs:CreateLogStream logs:PutLogEvents \
  --resource-arns '*'
```

#### Root Cause
IAM policy missing required CloudWatch Logs permissions. Policy had incorrect resource ARN format.

#### How I Fixed It
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "logs:CreateLogGroup",
      "logs:CreateLogStream",
      "logs:PutLogEvents"
    ],
    "Resource": "arn:aws:logs:*:*:*"
  }]
}
```

#### Before → After

| Metric | Before | After |
|--------|--------|-------|
| **IAM Policy** | Missing CloudWatch actions | All 3 actions granted |
| **CloudWatch Logs** | Silent failure (no logs) | ✅ Log stream active |
| **Error Messages** | AccessDeniedException | Logs written successfully |

**Key Learning:** IAM errors are frustrating but teach you to read AWS documentation carefully and use Policy Simulator.

[**Full Walkthrough →**](scenarios/iam_permissions.md)

---

### 5️⃣ GuardDuty Security Findings

**What I Learned:** Incident response workflow and security best practices

![GuardDuty Dashboard](https://raw.githubusercontent.com/charles-bucher/AWS_Cloud_Support_Sim/main/screenshots/guardduty-findings.png)

#### Problem I Created
Intentionally triggered GuardDuty alerts to practice incident response.

#### Investigation Process
```bash
# 1. Listed GuardDuty findings
aws guardduty list-findings --detector-id xxxx

# 2. Got finding details
aws guardduty get-findings \
  --detector-id xxxx \
  --finding-ids "finding-id-here"

# 3. Checked CloudTrail for suspicious activity
aws cloudtrail lookup-events \
  --lookup-attributes AttributeKey=Username,AttributeValue=compromised-user

# 4. Identified affected resources
aws iam list-access-keys --user-name compromised-user
```

#### Root Cause
Simulated compromised IAM access key making unusual API calls.

#### How I Responded (Incident Response Timeline)
```
⏰ T+0 min:  GuardDuty finding detected
⏰ T+2 min:  Reviewed finding details and severity
⏰ T+5 min:  Identified compromised access key via CloudTrail
⏰ T+8 min:  Deactivated access key immediately
⏰ T+10 min: Rotated to new secure key
⏰ T+15 min: Reviewed all API calls from compromised key
⏰ T+20 min: Tightened Security Group rules
⏰ T+25 min: Enabled MFA on root account (should've done first!)
⏰ T+30 min: Configured SNS alerts for future findings
⏰ T+40 min: Documented incident and created runbook
```

#### Remediation Actions Taken
```bash
# 1. Deactivated compromised access key
aws iam update-access-key \
  --access-key-id AKIAEXAMPLE \
  --status Inactive \
  --user-name compromised-user

# 2. Created new access key
aws iam create-access-key --user-name compromised-user

# 3. Updated Security Group rules
aws ec2 revoke-security-group-ingress \
  --group-id sg-xxxx \
  --protocol tcp \
  --port 22 \
  --cidr 0.0.0.0/0  # Removed overly permissive rule

# 4. Enabled MFA on root account (via Console)

# 5. Set up SNS alerts
aws sns create-topic --name guardduty-alerts
aws guardduty create-filter --detector-id xxxx \
  --action ARCHIVE \
  --finding-criteria ...
```

#### Before → After

| Metric | Before | After |
|--------|--------|-------|
| **Access Key Status** | Active (compromised) | ✅ Rotated to new key |
| **Security Groups** | 0.0.0.0/0 SSH access | My IP only |
| **MFA** | Disabled on root | ✅ Enabled |
| **Alerting** | No notifications | ✅ SNS email alerts |
| **Recurrence** | N/A | 0 further incidents |

**Key Learning:** Security incidents have a methodical response process. Stay calm, follow the checklist, document everything.

[**Full Walkthrough →**](scenarios/guardduty_alerts.md)

---

## 🚀 Quick Start

### ⚠️ Warning
This deploys **real AWS resources**. Use Free Tier or expect small charges (~$5-10/month).

### Prerequisites

```bash
# Required
✅ AWS Account (Free Tier works)
✅ AWS CLI v2 configured with credentials
✅ Terraform v1.0+ installed
✅ Basic Linux/terminal knowledge

# Optional
✅ Python 3.8+ for automation scripts
✅ Git for version control
```

### Deploy Lab Environment

```bash
# 1. Clone repository
git clone https://github.com/charles-bucher/AWS_Cloud_Support_Sim.git
cd AWS_Cloud_Support_Sim

# 2. Navigate to Terraform directory
cd iac

# 3. Initialize Terraform
terraform init

# 4. Review what will be created
terraform plan

# 5. Deploy infrastructure (creates real AWS resources!)
terraform apply

# When prompted, type 'yes' to confirm

# 6. Save outputs (includes IPs, IDs, etc.)
terraform output > ../terraform-outputs.txt

# 7. When done learning, destroy to avoid charges
terraform destroy
# When prompted, type 'yes' to confirm
```

### Verify Deployment

```bash
# Check VPC created
aws ec2 describe-vpcs --filters "Name=tag:Name,Values=cloud-support-sim-vpc"

# Check EC2 instance
aws ec2 describe-instances --filters "Name=tag:Name,Values=cloud-support-sim-instance"

# Check S3 bucket
aws s3 ls | grep cloud-support-sim

# Check Lambda function
aws lambda list-functions | grep cloud-support-sim
```

---

## 📁 Project Structure

```
AWS_Cloud_Support_Sim/
│
├── iac/                           # Infrastructure as Code
│   ├── main.tf                    # Core Terraform configuration
│   ├── variables.tf               # Input variables
│   ├── outputs.tf                 # Output values
│   ├── vpc.tf                     # VPC and networking
│   ├── ec2.tf                     # EC2 instances
│   ├── s3.tf                      # S3 buckets
│   ├── lambda.tf                  # Lambda functions
│   ├── iam.tf                     # IAM roles and policies
│   └── guardduty.tf               # GuardDuty configuration
│
├── scenarios/                     # Learning scenarios with walkthroughs
│   ├── ec2_connectivity.md        # EC2 SSH troubleshooting
│   ├── s3_access_denied.md        # S3 permission debugging
│   ├── lambda_timeout.md          # Lambda performance optimization
│   ├── iam_permissions.md         # IAM policy troubleshooting
│   └── guardduty_alerts.md        # Security incident response
│
├── runbooks/                      # Operational runbooks
│   ├── RB-001_ec2_connectivity.md
│   ├── RB-002_s3_permissions.md
│   ├── RB-003_lambda_timeout.md
│   ├── RB-004_iam_debugging.md
│   └── RB-005_security_response.md
│
├── scripts/                       # Automation scripts
│   ├── deploy_infrastructure.sh   # Deployment automation
│   ├── simulate_errors.py         # Error simulation for practice
│   ├── remediation.py             # Automated remediation
│   ├── monitoring_setup.py        # CloudWatch setup
│   └── cleanup.sh                 # Resource cleanup
│
├── tests/                         # Validation tests
│   ├── test_connectivity.py
│   ├── test_permissions.py
│   └── test_lambda.py
│
├── diagrams/                      # Architecture diagrams
│   ├── lab-environment.png
│   ├── vpc-architecture.png
│   ├── incident-workflow.png
│   └── monitoring-setup.png
│
├── screenshots/                   # Evidence of work
│   ├── ec2-security-groups.png
│   ├── s3-bucket-config.png
│   ├── cloudwatch-lambda-metrics.png
│   ├── iam-role-policies.png
│   └── guardduty-findings.png
│
├── docs/                          # Additional documentation
│   ├── setup-guide.md
│   ├── troubleshooting-tips.md
│   └── cost-breakdown.md
│
├── .github/                       # GitHub configuration
│   └── workflows/
│       └── terraform-validate.yml # CI/CD validation
│
├── requirements.txt               # Python dependencies
├── .gitignore                     # Git ignore patterns
├── .terraform.lock.hcl            # Terraform lock file
├── README.md                      # This file
├── LICENSE.md                     # MIT License
├── CODE_OF_CONDUCT.md            # Code of conduct
├── CONTRIBUTING.md                # Contribution guidelines
└── SECURITY.md                    # Security policy
```

---

## 🛠️ Technologies

### Cloud Platform
![AWS](https://img.shields.io/badge/AWS-Cloud-FF9900?style=flat-square&logo=amazon-aws)

**Services Used:**
- **Compute:** EC2, Lambda
- **Storage:** S3, EBS
- **Networking:** VPC, Security Groups, NACLs, Route Tables
- **Security:** IAM, GuardDuty, CloudTrail
- **Monitoring:** CloudWatch (Logs, Metrics, Alarms)

### Infrastructure & Automation
![Terraform](https://img.shields.io/badge/Terraform-IaC-7B42BC?style=flat-square&logo=terraform)
![Python](https://img.shields.io/badge/Python-Scripting-3776AB?style=flat-square&logo=python)
![Bash](https://img.shields.io/badge/Bash-Automation-4EAA25?style=flat-square&logo=gnu-bash)

### Development Tools
![Git](https://img.shields.io/badge/Git-Version_Control-F05032?style=flat-square&logo=git)
![VS Code](https://img.shields.io/badge/VS_Code-Editor-007ACC?style=flat-square&logo=visual-studio-code)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=flat-square&logo=ubuntu)

---

## 📚 What I'm Currently Learning

### Active Study (January 2025)

**AWS Solutions Architect - Associate Certification**
- 📖 Following Stephane Maarek's Udemy course
- 🧪 Hands-on labs from Tutorials Dojo
- 📝 Building this project to reinforce concepts
- 🎯 No exam date scheduled yet (learning first!)

### Next Skills on Roadmap

```
Q1 2025:
├─ CloudFormation (alternative IaC)
├─ Auto Scaling Groups & Load Balancers
├─ Container basics (ECS)
└─ CI/CD pipeline fundamentals

Q2 2025:
├─ Take AWS SAA exam
├─ AWS SysOps Administrator Associate prep
├─ Advanced monitoring patterns
└─ Cost optimization strategies
```

### Resources I Use

**Free:**
- AWS Free Tier
- AWS Documentation
- YouTube (specific topics only, not full courses)
- Reddit r/AWSCertifications community

**Paid (~$45/month):**
- Udemy courses ($10-15 one-time)
- Tutorials Dojo practice exams ($15 one-time)
- AWS account costs (~$20/month for lab)

---

## 🎯 Career Goals

### What I'm Looking For

**Target Roles:**
- AWS Cloud Support Associate
- Junior SysOps Administrator
- Cloud Operations Engineer (Entry-level)
- Technical Support Engineer (Cloud)

**Compensation:**
- **Year 1:** $50k-$65k (realistic entry-level)
- **Years 2-3:** $70k-$90k combined household income
- **Years 4-5:** $100k individual

**Location:**
- Remote preferred (Florida-based)
- Open to hybrid if Tampa Bay area
- Willing to consider contract/staffing agencies

**Availability:** Immediate (2-week notice to current employer)

---

### Why Hire Me?

**What I Bring:**
- ✅ **Hands-on AWS experience** (this repo proves it with screenshots, code, docs)
- ✅ **Self-motivated** (taught myself while working full-time delivery)
- ✅ **Documentation skills** (professional runbooks and incident reports)
- ✅ **Problem-solving mindset** (systematic troubleshooting approach)
- ✅ **Humble and eager** (know I'm entry-level, ready to learn)

**What I Need:**
- ✅ Chance to prove myself in entry-level role
- ✅ Company that values demonstrated skills over credentials
- ✅ Environment where I can continue learning

**What Makes Me Different:**
- I'm not claiming 5 years experience I don't have
- Every screenshot in this repo is from MY AWS account
- I spent MY money ($20/month) to learn
- I built this after MY 10-hour delivery shifts
- I'm honest about being entry-level and my background

---

## 📞 Contact

**Charles Bucher**  
Self-Taught Cloud Engineer | Open to Work

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/charles-bucher-cloud)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)](https://github.com/charles-bucher)
[![Email](https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge&logo=gmail)](mailto:quietopscb@gmail.com)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-4A90E2?style=for-the-badge)](https://charles-bucher.github.io)

📧 **Email:** quietopscb@gmail.com  
💼 **LinkedIn:** [linkedin.com/in/charles-bucher-cloud](https://linkedin.com/in/charles-bucher-cloud)  
🌐 **Portfolio:** [charles-bucher.github.io](https://charles-bucher.github.io)

---

## 🔬 Verifiable Work

**AWS Account:** `722631436033` (verifiable live infrastructure)  
**Monthly Investment:** $20/month self-funded lab  
**Contributions:** 397 commits this year  
**Lab Runtime:** December 2024 - Present

**All screenshots are from MY AWS account. No stock images. No tutorial screenshots. Just my real work.**

---

## 📄 License

MIT License - See [LICENSE.md](LICENSE.md) for details.

You're free to use this project for learning, but please:
- ⭐ Star the repo if you find it useful
- 🔗 Give credit if you adapt it for your own portfolio
- 💬 Share feedback through Issues

---

## 🙏 The Truth

### I'm Self-Taught (No Hiding It)
- This is a learning project, not production-grade infrastructure
- I'm entry-level, not senior (and I'm okay with that)
- I have a felony record from 2003 (clean since 2008, now 22 years later)
- I'm 40 with three kids—no time for BS or fake claims

### But Here's What's Real
- ✅ Every screenshot is from MY AWS account (722631436033)
- ✅ I spent MY money learning (~$20/month)
- ✅ I built this after MY 10-hour delivery shifts
- ✅ This is MY actual learning journey

### Bottom Line
**I can't fake experience, so I'm building proof.**

If you value hands-on skills, systematic thinking, and someone who will work twice as hard to prove themselves—I'm your candidate.

---

## ⭐ Support This Project

If you find this helpful:
- ⭐ **Star this repository** to help others discover it
- 🔗 **Share with others** learning cloud operations
- 💬 **Provide feedback** through Issues or Discussions
- 🤝 **Connect on LinkedIn** if you're hiring entry-level cloud engineers

---

<div align="center">

**Built with ☕, determination, and real AWS infrastructure**

![GitHub Stars](https://img.shields.io/github/stars/charles-bucher/AWS_Cloud_Support_Sim?style=social)
![GitHub Forks](https://img.shields.io/github/forks/charles-bucher/AWS_Cloud_Support_Sim?style=social)

**Charles Bucher** | Self-Taught Cloud Engineer

*"I can't fake experience, so I'm building proof."*

</div>