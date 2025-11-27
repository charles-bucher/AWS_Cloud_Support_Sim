# AWS Lambda Error Scenario Instructions

## Objective
Simulate and troubleshoot an AWS Lambda function error to demonstrate error handling and debugging skills.

## Scenario
You have a Lambda function that is supposed to process events from an S3 bucket (or another source). The function currently fails due to an intentional or unintentional error.

## Tasks

1. **Setup**
   - Ensure you have AWS CLI configured with appropriate permissions.
   - Navigate to this directory in your terminal.

2. **Deploy Lambda Function**
   - Use the provided `lambda_function.py` (or relevant code) to create a Lambda function.
   - Deploy it manually via AWS Console or using a CloudFormation/Terraform template.

3. **Trigger Error**
   - Upload a test event to the Lambda source (e.g., S3 bucket, API Gateway).
   - Observe the Lambda execution failure in the CloudWatch logs.

4. **Troubleshoot**
   - Review the logs in CloudWatch to identify the error cause.
   - Common issues could include:
     - Missing IAM permissions
     - Runtime exceptions in the code
     - Invalid input events

5. **Fix**
   - Update the Lambda code or permissions to resolve the error.
   - Redeploy and retest to confirm the function executes successfully.

6. **Documentation**
   - Write a short summary of the error, the debugging steps you took, and the solution.
   - Optionally, add screenshots of CloudWatch logs and successful execution.

## Notes
- This exercise demonstrates your ability to identify, debug, and fix Lambda issues.
- Keep the portfolio updated with clear explanations for recruiters or interviewers.

