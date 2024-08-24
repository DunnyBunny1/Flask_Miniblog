from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm): 
    """
    A Flask web form for user login. Includes class variables for each login field: a username, password, a "remember me" check, and a submit button.
    """
    # Required fields - ensure the data submitted is nonempty
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    # A checkbox to see if logged in users should be persisted 
    remember_me = BooleanField('Remember Me')
    # A button to trigger a sign-in request 
    submit = SubmitField('Sign In')
