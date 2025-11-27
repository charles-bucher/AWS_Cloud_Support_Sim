# S3 IAM Access Scenario Instructions

## Objective
Demonstrate your ability to configure and troubleshoot AWS IAM permissions for accessing an S3 bucket.

## Scenario
You are given an S3 bucket with restricted access. A user or Lambda function needs permission to read, write, or list objects in this bucket. Currently, the access is failing due to IAM misconfigurations.

## Tasks

1. **Setup**
   - Make sure you have AWS CLI installed and configured with credentials that have IAM and S3 access.
   - Navigate to this scenario directory in your terminal.

2. **Review Current IAM Policies**
   - Identify which IAM user, role, or group is being used.
   - Check the existing policies attached to the IAM entity.
   - Examine the S3 bucket policy if one exists.

3. **Simulate Access Failure**
   - Attempt to access the S3 bucket using the current IAM user/role:
     ```bash
     aws s3 ls s3://<bucket-name>/
     ```
   - Record the error message (e.g., `AccessDenied`).

4. **Troubleshoot**
   - Analyze IAM policies and bucket policies to find the missing permission.
   - Check for common issues:
     - Missing `s3:GetObject`, `s3:PutObject`, or `s3:ListBucket` actions.
     - Deny statements overriding allow statements.
     - Role not assumed properly (if using Lambda or EC2 instance profile).

5. **Fix Permissions**
   - Update the IAM policy or bucket policy to allow the required access.
   - Example IAM policy snippet:
     ```json
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Effect": "Allow",
           "Action": [
             "s3:GetObject",
             "s3:PutObject",
             "s3:ListBucket"
           ],
           "Resource": [
             "arn:aws:s3:::<bucket-name>",
             "arn:aws:s3:::<bucket-name>/*"
           ]
         }
       ]
     }
     ```

6. **Validate Access**
   - Re-run the `aws s3 ls` or relevant S3 command to ensure access works.
   - Confirm that read/write operations succeed.

7. **Documentation**
   - Summarize the original issue, your troubleshooting steps, and the final fix.
   - Optionally, include screenshots of the IAM console, policies, or successful S3 operations.

## Notes
- This scenario tests your understanding of AWS IAM permissions and S3 access control.
- Clear documentation of the problem-solving steps will strengthen your portfolio.
