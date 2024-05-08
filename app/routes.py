from app import app
from flask import render_template


@app.route("/")
@app.route("/index")
# This view function will be triggered whenever either endpoint specified
# above is requested when a browser requests this URL. The return
# value of the function will be returned to the browser
def index():
    # Create a mock user
    user = {"username": "Miguel"}
    posts = get_posts()
    return render_template("index.html", title="Home", user=user, posts= posts)

def get_posts(): 
    return [ 
        {'author' : {'username' : 'John'},'body' : 'Beautiful Day in Boston!'},
        {'author' : {'username' : 'Susan'}, 'body' : 'That movie was tuff'},
        {'author' : {'username' : 'Bob'}, 'body' : 'The Celtics are the greatest team in the world'},
    ]