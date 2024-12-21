# Basic Python script for demonstration

def greet_user(name):
    Returns a greeting message for the given user.

    Args:
        name (str): The name of the user.

    Returns:
        str: A greeting message.
    return f"Hello, {name}!"

if __name__ == "__main__":
    user_name = input("Enter your name: ").strip()
    is not user_name:
    print("No name entered. Please provide a valid name.")
else:
    print(greet_user(user_name))