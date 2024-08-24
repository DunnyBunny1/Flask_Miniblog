# Python to define our application instance
# Import our "api" flask application instance from the app package,
# which will trigger its __init__.py file
from app import api
api.run(debug=True)