""" Question 41. Write a flask app that accepts a parameter in the url and display it on the page."""


from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the home page!"

@app.route('/show/<parameter>')
def show(parameter):
    return f'The parameter you passed is: {parameter}'

if __name__ == '__main__':
    app.run(debug=True)


"""Access the URL: Open your web browser and go to http://127.0.0.1:5000/show/your_parameter_here. 
Replace your_parameter_here with any value you want to pass as a parameter."""