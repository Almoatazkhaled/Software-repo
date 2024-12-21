# Basic Python script for demonstration

def farewell_user(name):
    
    Returns a farewell message for the given user.

    Args:
        name (str): The name of the user.

    Returns:
        str: A farewell message.
    
    return f"Goodbye, {name}! See you next time."

if __name__ == "__main__":
    user_name = input("Enter your name: ").strip()
    if not user_name:
        print("No name entered. Please provide a valid name.")
    else:
        print(greet_user(user_name))
        print(farewell_user(user_name))
