"""Question 44. How would you create a RESTful API endpoint in Flask that returns JSON data."""

from flask import Flask, jsonify

# Initialize the Flask application
RESTful_API = Flask(__name__)

# Sample data
users = [
    {'id': 1, 'username': 'john_doe', 'email': 'john@example.com'},
    {'id': 2, 'username': 'jane_doe', 'email': 'jane@example.com'}
]

# Define a route to return JSON data
@RESTful_API.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Run the app
if __name__ == '__main__':
    RESTful_API.run(debug=True)


"""With this setup, when you navigate to http://127.0.0.1:5000/api/users,
the application will return the JSON array of users:"""

"""[
    {
        "id": 1,
        "username": "john_doe",
        "email": "john@example.com"
    },
    {
        "id": 2,
        "username": "jane_doe",
        "email": "jane@example.com"
    }
]

"""