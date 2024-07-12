"""_summary_ Question 40. Explain how to set up a flask application to handle form submission using POST request.
    """


## in flask we can use POST method to handle form submision.
## Following application is the simple example of post method.

from flask import Flask, render_template, request

app_post=Flask(__name__)

@app_post.route('/')
def index():
    return render_template('FormSubmission.html')

@app_post.route('/FormData', methods=["POST", "GET"])
def formdata():
    if request.method=="POST":
        text=request.form.get('Data')
        return f'Data Collected: {text} '
    

if __name__=="__main__":
    app_post.run(debug=True)    