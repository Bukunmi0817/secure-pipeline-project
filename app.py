import os
from vault import get_secret

def greet(name):
    return f"Hello, {name}!"

def main():
    # Get secrets from AWS Secrets Manager
    secrets = get_secret("myapp/secrets")
    
    # Use secret value securely
    db_password = secrets["DB_PASSWORD"]
    print(f"Database connection secured ✓")
    
    # Normal app logic
    name = os.environ.get("APP_NAME", "World")
    message = greet(name)
    print(message)

if __name__ == "__main__":
    main()