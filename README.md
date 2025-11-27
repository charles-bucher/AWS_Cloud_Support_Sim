# AWS Cloud Support Portfolio

![AWS](https://img.shields.io/badge/AWS-Cloud-yellow)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Terraform](https://img.shields.io/badge/Terraform-HCL-lightgrey)
![Portfolio](https://img.shields.io/badge/Portfolio-Ready-green)

This repository showcases **hands-on troubleshooting scenarios for AWS services**, demonstrating practical skills in EC2, Lambda, S3, IAM, and more. It is designed for entry-level cloud support and NOC positions, simulating real-world support workflows from initial issue to resolution.

---

## Table of Contents
- [EC2 Troubleshooting](#ec2-troubleshooting)
- [Lambda Error Handling](#lambda-error-handling)
- [S3 IAM Access](#s3-iam-access)
- [Screenshots](#screenshots)
- [Contact](#contact)

---

## EC2 Troubleshooting

**Scenario:** Launch an EC2 instance via CloudFormation, verify connectivity, and troubleshoot security group issues.

**Files:**
- `scenarios/ec2-troubleshoot/cloudformation.yaml` – CloudFormation template
- `scenarios/ec2-troubleshoot/ec2-troubleshoot.txt` – Step-by-step notes
- `scenarios/ec2-troubleshoot/instructions.md` – Instructions

**Key Steps:**
1. Deploy CloudFormation stack
2. Verify EC2 instance creation
3. Configure and check Security Groups
4. Test connectivity using ping and SSH

**Screenshots:**
![Stack Created](docs/screenshots/ec2-stack-created.png)
![Security Group Config](docs/screenshots/ec2-sg-config.png)
![Ping Test](docs/screenshots/ec2-ping-test.png)

**Skills Demonstrated:**
- EC2 instance deployment
- Security group troubleshooting
- SSH connectivity verification
- CloudFormation understanding

---

## Lambda Error Handling

**Scenario:** Diagnose and resolve a Lambda function error.

**Files:**
- `scenarios/lambda-error/instructions.md`

**Key Steps:**
1. Deploy the Lambda function
2. Trigger an error event
3. Analyze CloudWatch logs
4. Update code or IAM permissions
5. Redeploy and test success

**Screenshots:**
![Lambda Error](docs/screenshots/lambda-error-log.png)
![Lambda Success](docs/screenshots/lambda-success.png)

**Skills Demonstrated:**
- Lambda deployment and debugging
- IAM permission troubleshooting
- CloudWatch log analysis

---

## S3 IAM Access

**Scenario:** Troubleshoot S3 bucket access using IAM policies.

**Files:**
- `scenarios/s3-iam-access/instructions.md`

**Key Steps:**
1. Identify IAM user or role
2. Review policies and bucket permissions
3. Simulate access failure via CLI
4. Update IAM or bucket policy
5. Verify access

**Screenshots:**
![S3 Access Denied](docs/screenshots/s3-access-denied.png)
![S3 Access Success](docs/screenshots/s3-access-success.png)

**Skills Demonstrated:**
- IAM policy debugging
- S3 access control
- AWS CLI operations

---

## Screenshots Overview
All screenshots are stored in `docs/screenshots/`. They demonstrate:
- CloudFormation stack creation
- EC2 instance deployment and connectivity
- Lambda debugging and resolution
- IAM/S3 access troubleshooting

---

## Contact
**Charles Bucher**  
[GitHub](https://github.com/charles-bucher) | [LinkedIn](https://www.linkedin.com/in/charles-bucher)

---

## About
This portfolio simulates a **Cloud Support Engineer workflow**, documenting real-world AWS troubleshooting scenarios. Each case study follows a support ticket lifecycle from customer report to root cause analysis and resolution.

**Topics:** terraform, incident-response, cloudwatch, ci-cd, infrastructure-as-code, aws-security, noc, cloudops, cloud-support, python-automation
