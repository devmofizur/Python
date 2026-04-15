from functools import wraps

user_status = {
    "is_logged_in": False,
    "username": "Rakib"
}

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if user_status["is_logged_in"]:
            return func(*args, **kwargs) 
        else:
            print("Error: Login First!")
    return wrapper

@login_required
def view_profile():
    print(f"Welcome, {user_status['username']}")

@login_required
def change_password():
    print("Change password success")

print("View Profile")
view_profile()

print("\nView Profile")
user_status["is_logged_in"] = True 
view_profile()
change_password()