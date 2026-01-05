import boto3

def get_account_info():
    sts = boto3.client("sts")
    identity = sts.get_caller_identity()
    print("AWS Account Info:")
    print(f"  Account ID: {identity['Account']}")
    print(f"  User ARN: {identity['Arn']}")
    print(f"  User ID: {identity['UserId']}\n")

def list_regions():
    ec2 = boto3.client("ec2")
    regions = [r['RegionName'] for r in ec2.describe_regions()['Regions']]
    print("AWS Regions:")
    print(f"  {', '.join(regions)}\n")
    return regions

def list_s3_buckets():
    s3 = boto3.client("s3")
    buckets = [b['Name'] for b in s3.list_buckets()['Buckets']]
    print("S3 Buckets:")
    print(f"  {', '.join(buckets) if buckets else 'None'}\n")

def list_ec2_instances():
    ec2 = boto3.client("ec2")
    instances = []
    for r in list_regions():
        regional_ec2 = boto3.client("ec2", region_name=r)
        res = regional_ec2.describe_instances()
        for reservation in res['Reservations']:
            for instance in reservation['Instances']:
                instances.append({
                    "ID": instance['InstanceId'],
                    "Type": instance['InstanceType'],
                    "State": instance['State']['Name'],
                    "Region": r
                })
    print("EC2 Instances:")
    if instances:
        for i in instances:
            print(f"  {i['ID']} | {i['Type']} | {i['State']} | {i['Region']}")
    else:
        print("  None")
    print()

def list_lambda_functions():
    functions = []
    for r in list_regions():
        lambda_client = boto3.client("lambda", region_name=r)
        res = lambda_client.list_functions()
        for func in res.get('Functions', []):
            functions.append({
                "Name": func['FunctionName'],
                "Runtime": func['Runtime'],
                "Region": r
            })
    print("Lambda Functions:")
    if functions:
        for f in functions:
            print(f"  {f['Name']} | {f['Runtime']} | {f['Region']}")
    else:
        print("  None")
    print()

if __name__ == "__main__":
    get_account_info()
    list_s3_buckets()
    list_ec2_instances()
    list_lambda_functions()
