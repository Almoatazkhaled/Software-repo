# example.py
from datetime import datetime

def greet(name):
    if not name.isalpha():
        raise ValueError("Name should only contain alphabets")
    
    hour = datetime.now().hour
    if hour < 12:
        return f"Good morning, {name}!"
    elif hour < 18:
        return f"Good afternoon, {name}!"
    else:
        return f"Good evening, {name}!"

def farewell(name):
    if not name.isalpha():
        raise ValueError("Name should only contain alphabets")
    return f"Goodbye, {name}!"

if __name__ == "__main__":
    try:
        print(greet("World"))
        print(farewell("World"))
    except ValueError as e:
        print(e)
