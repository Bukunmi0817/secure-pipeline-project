import boto3
import json
from botocore.exceptions import ClientError

def get_secret(secret_name: str) -> dict:
    client = boto3.client("secretsmanager", region_name="eu-north-1")
    
    try:
        response = client.get_secret_value(SecretId=secret_name)
        secret = json.loads(response["SecretString"])
        return secret
    except ClientError as e:
        raise Exception(f"Failed to retrieve secret: {e}")

if __name__ == "__main__":
    secrets = get_secret("myapp/secrets")
    print(f"Secret retrieved successfully")
    print(f"Keys available: {list(secrets.keys())}")