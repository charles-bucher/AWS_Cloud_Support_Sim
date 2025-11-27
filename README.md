⚡ Cloud Support Simulation Portfolio

👋 Hi, I’m Charles Bucher — a self-taught Cloud Support & NOC Engineer.
This repo simulates real AWS support workflows: incidents, troubleshooting, investigations, fixes, and validations.
Everything here mirrors what junior cloud engineers, NOC analysts, and L1/L2 support specialists do every day.

🚀 What This Portfolio Demonstrates

EC2 troubleshooting (SG issues, connectivity, provisioning failures)

Lambda error analysis (CloudWatch logs, IAM failures, code bugs)

S3 & IAM access debugging (permissions, bucket policies, CLI testing)

Operational workflows (root-cause analysis, structured incident handling)

Automation & IaC (Terraform, Python, CloudFormation)

Version control discipline (Git, GitHub Actions)

This is the “I actually know how to troubleshoot cloud systems” repo.

🛠️ Core Skills Demonstrated
Category	Skills
AWS Services	EC2, Lambda, S3, IAM, CloudWatch, CloudFormation
Automation & IaC	Terraform, Python scripting
Monitoring & Logging	CloudWatch metrics & log analysis
Operational Troubleshooting	Incident simulation, RCA, SLA thinking
Version Control / DevOps	Git, GitHub Actions
📂 Portfolio Scenarios (with embedded screenshots)
1️⃣ EC2 Troubleshooting

Objective: Launch an EC2 instance using CloudFormation and verify connectivity.

Key Steps

Deploy CloudFormation stack

Verify EC2 provisioning

Configure & troubleshoot Security Groups

Test connectivity (SSH / ping)

Validate root cause and resolution

🔍 Screenshots
EC2 Creation

Security Group Debugging

2️⃣ Lambda Error Handling

Objective: Diagnose and resolve Lambda execution failures.

Key Steps

Deploy Lambda function

Trigger a controlled error

Investigate CloudWatch logs

Fix IAM policy or function code

Redeploy and validate success

🔍 Screenshots
Lambda Error in Console

CloudWatch Log Investigation

3️⃣ S3 IAM Access Debugging

Objective: Troubleshoot access denied issues for an IAM user accessing S3.

Key Steps

Identify IAM user/role

Review IAM policy and bucket policy

Reproduce failure using AWS CLI

Update permissions

Validate successful access

🔍 Screenshots
Access Denied

Policy Fix Applied

📁 Repository Structure
AWS_Cloud_Support_Sim/
├── docs/
│   └── screenshots/        # All scenario screenshots
├── scenarios/              # EC2, Lambda, S3 troubleshooting exercises
├── src/AWS_Project/        # Python automation scripts
├── main.py                 # Python entry point
├── utils.py                # Helpers
├── main.tf                 # Terraform template
├── requirements.txt        # Python dependencies
└── README.md               # This file

📬 Contact

Email: quietopscb@gmail.com

GitHub: https://github.com/charles-bucher

LinkedIn: https://www.linkedin.com/in/charles-bucher-cloud

💡 Notes

All scenarios mirror real production troubleshooting patterns

Costs can apply when provisioning AWS resources — clean them up

Screenshots show reproducible steps and validated fixes
