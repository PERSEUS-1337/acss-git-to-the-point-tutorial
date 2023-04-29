# User Authentication System

This Python code provides a simple user authentication system for the space station's computer system.

## Files

- `auth.py`: Contains functions for hashing and checking passwords.
- `user.py`: Defines the `User` class for creating and authenticating users.
- `main.py`: Implements the user authentication system.

## Usage

To use this authentication system, follow these steps:

1. Import the `User` class from the `user.py` file.
2. Create a new user object by passing in a username and password.
3. Call the `authenticate` method on the user object, passing in the password to check.
4. Check the `is_authenticated` attribute on the user object to see if authentication was successful.

Example:

```python
from user import User

# Create a user
user = User('admin', 'password123')

# Authenticate the user
if user.authenticate('password123'):
    print('User authenticated successfully.')
else:
    print('Invalid username or password.')
```