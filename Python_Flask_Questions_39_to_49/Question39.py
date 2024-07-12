"""_summary_ Question 39. How would you create a basic flask route that displays "Hello, World!" on the homepage?
    """


## Creating simple flask app that display Hello, world!  
from flask import Flask

hello_world=Flask(__name__)

@hello_world.route('/')
def hello():
    return "Hello, World!"

if __name__=="__main__":
    hello_world.run(debug=True)    