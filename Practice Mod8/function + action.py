'''
Q1 — Purpose + Action
Write a function greet_user(name) that:
- Takes a person's name as input.
- Prints a greeting message.
- Example: greet_user("Ali") → Hello, Ali!
'''
def greet_message(name):
    username = f"Hello, {name}"
    print(username)
    
user_name = input("Enter your name:")
greet_message(user_name)
