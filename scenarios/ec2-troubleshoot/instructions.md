# EC2 Troubleshooting Scenario Instructions

## Objective
Demonstrate your ability to diagnose and resolve common AWS EC2 instance issues, including connectivity, service failures, and resource configuration problems.

## Scenario
An EC2 instance is not functioning as expected. It could be failing to start, be unreachable via SSH/RDP, or have application/service issues. Your task is to identify the root cause and implement a fix.

## Tasks

1. **Setup**
   - Ensure your AWS CLI is configured with permissions to manage EC2 instances.
   - Identify the target EC2 instance by Instance ID or Name Tag.

2. **Identify the Problem**
   - Check instance state in the AWS Console or CLI:
     ```bash
     aws ec2 describe-instances --instance-ids <instance-id>
     ```
   - Look for common issues:
     - Instance stuck in `pending` or `stopping` state.
     - System or instance status checks failing.
     - Misconfigured security groups or network ACLs.

3. **Connectivity Troubleshooting**
   - Verify security group rules allow SSH (port 22) or RDP (port 3389) access from your IP.
   - Check the instance’s public/private IP and subnet routing.
   - Use the EC2 Serial Console (if enabled) for boot-level troubleshooting.

4. **Application/Service Troubleshooting**
   - SSH or RDP into the instance if possible.
   - Check system logs for errors:
     ```bash
     sudo tail -n 100 /var/log/syslog       # Linux
     Get-EventLog -LogName System           # Windows PowerShell
     ```
   - Restart failed services or check configuration files as needed.

5. **Resource or Configuration Issues**
   - Verify EBS volume attachments and space usage.
   - Check IAM roles attached to the instance if accessing other AWS resources.
   - Ensure OS updates or firewall settings are not causing failures.

6. **Fix the Issue**
   - Apply the necessary corrections (security group changes, restarting services, adjusting IAM role, etc.).
   - Validate that the EC2 instance becomes reachable and services operate normally.

7. **Documentation**
   - Summarize the initial problem, diagnostic steps, root cause, and the solution.
   - Include screenshots or command outputs where applicable to demonstrate troubleshooting steps.

## Notes
- This scenario is meant to demonstrate hands-on EC2 troubleshooting skills for your portfolio.
- Clear documentation of both the problem and the fix is critical for recruiters or interviewers to understand your process.
