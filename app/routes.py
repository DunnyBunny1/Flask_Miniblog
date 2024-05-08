from app import app

@app.route('/')
@app.route('/index')
# This index view function will be triggered whenever either endpoint
# specified above is requested when a browser requests this URL. The return
# value of the function will be returned to the browser 
def index():
    return 'Hello, World!'