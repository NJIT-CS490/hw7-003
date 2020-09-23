import flask
import os
import random

app = flask.Flask(__name__)
picturelst=[
    "NJIT Logo.png",
    "Eberhardt Hall.JPG"
]

@app.route('/') # Python decorator
def index():
    return flask.render_template(
        "index.html",
        pictures_lst=picturelst,
        random_index=random.randrange(0,len(picturelst))
    )
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)