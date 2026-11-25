# Import Flask framework and render_template function
from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)


# Define the home route (URL: /)
@app.route('/')
def hello_world():
    # Render and return the index.html template
    return render_template('index.html')


# Define the health check route (URL: /health)
@app.route('/health')
def health():
    # Return a message to check whether the server is running
    return 'Server is up and running'
