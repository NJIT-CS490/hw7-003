import flask
import os
import random
import requests
import datetime


app = flask.Flask(__name__)
picturelst=[
    "NJIT Logo.png",
    "Eberhardt Hall.JPG"
]

@app.route('/') # Python decorator
def index():
    x = datetime.datetime.now()
    
    day=x.strftime("%B")
    page = 1
    all_commits = []
    commits = requests.get('https://api.github.com/repos/NJIT-CS490/hw7-003/commits?per_page=100&page=' + str(page)).json()
    
    while len(commits) > 0:
        all_commits += commits
        page += 1
        commits = requests.get('https://api.github.com/repos/NJIT-CS490/hw7-003/commits?per_page=100&page=' + str(page)).json()
    
    return flask.render_template(
        "index.html",
        pictures_lst=picturelst,
        today=day,
        random_index=random.randrange(0,len(picturelst)),
        commits=all_commits
    )

@app.route('/secret')
def secret():
    return flask.render_template("secret.html")    
    
app.run(
    debug=True,
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)