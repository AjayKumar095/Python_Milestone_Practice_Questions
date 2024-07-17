from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# MongoDB connection setup
# Replace Username and Password with you actual usename and password for mongodb client or database.

client = MongoClient('mongodb+srv://<Username>:<Password>m@cluster0.wxxmacs.mongodb.net/?retryWrites=true&w=majority')
db = client['mydatabase']  # Replace 'mydatabase' with your database name
users_collection = db['users']  # Collection for storing user data

@app.route('/')
def index():
    return 'Welcome to the Flask MongoDB Authentication Example'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Check if username already exists
        if users_collection.find_one({'username': username}):
            return 'Username already exists!'
        
        # Hash the password
        hashed_password = generate_password_hash(password)
        
        # Store the user in the database
        users_collection.insert_one({
            'username': username,
            'password': hashed_password
        })
        
        return 'User successfully registered!'
    
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Check if username exists in database
        user = users_collection.find_one({'username': username})
        
        if user and check_password_hash(user['password'], password):
            # Username and password are correct, set the session
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid username or password'
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return 'Hello Geeks'
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
