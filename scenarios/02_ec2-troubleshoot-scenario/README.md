EC2 Connectivity Troubleshooting Lab
README.md
🎯 Purpose
This lab teaches entry‑level cloud support engineers how to diagnose and resolve common EC2 connectivity issues using a structured, repeatable workflow. It mirrors real AWS support scenarios and emphasizes verification at every step.
🧩 Learning Objectives
- Understand how EC2 networking components interact (VPC, subnets, route tables, SGs, NACLs).
- Diagnose SSH/RDP connectivity failures.
- Validate routing, firewall rules, and OS‑level configuration.
- Use AWS CLI for troubleshooting and evidence gathering.
- Apply a professional runbook workflow.
🏗️ Architecture Overview
VPC (10.0.0.0/16)
│
├── Public Subnet (10.0.1.0/24)
│     ├── EC2 Instance (Amazon Linux 2)
│     └── IGW Route: 0.0.0.0/0 → igw-xxxx
│
└── Private Subnet (10.0.2.0/24)
      └── (Optional) EC2 for advanced scenarios




