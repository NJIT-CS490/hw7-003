import flask
import os
import random

app = flask.Flask(__name__)

@app.route('/') # Python decorator
def index():
    return flask.render_template("index.html")
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)