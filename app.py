import os

def greet(name):
    return f"Hello, {name}!"

def main():
    name = os.environ.get("APP_NAME", "World")
    message = greet(name)
    print(message)

if __name__ == "__main__":
    main()