# Basic Python script for demonstration

def greet_user(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet_user(user_name))