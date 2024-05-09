from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
# This view function will be triggered whenever either endpoint specified
# above is requested when a browser requests this URL. The return
# value of the function will be returned to the browser
def index():
    # Create a mock user
    user = {'username': 'DunnyBunny'}
    posts = [
        {"author": {"username": "John"}, "body": "Beautiful Day in Boston!"},
        {"author": {"username": "Susan"}, "body": "That movie was tuff"},
        {"author": {"username": "Bob"},"body": "The Celtics are the greatest team in the world"}
    ]

    return render_template("index.html", title="Home", user=user, posts=posts)

# Responds to POST and GET requests to the login endpoint submitting 
@app.route('/login',methods=['GET', 'POST'])
def login():
    form : LoginForm = LoginForm()
    print(form.validate_on_submit())
    # Indicates the user is submitting information via a POST request and the data has been validated, process the form information 
    if form.validate_on_submit():
        # Display a message to the user confirming receipt of the credentials
        flash(f'Login requested for user={form.username.data}, remember_me={form.remember_me.data}')
        # Redirect the user to the home page upon successful login 
        return redirect(url_for('index')) 
    
    # Otherwise, the user must be issuing a GET request to receive the sign-in page, or the user input is invalid. Transmit the empty form to the user
    else: 
        return render_template('login.html', title='Sign In',form=form)