# flask 
# is a framework for building servers
# contains all the component parts 
# flask and django are the main frameworks
# Flask is smaller but django has heaps of tools

# create a virtual env folder in your web server folder 
# cd one level above web sevrer folder
# python3 -m venv web\ server/
# creates a venv in the web server folder
# Activate the venv:
# source web\ server/bin/activate 
# the exact command depends on the type of shell being used
# https://docs.python.org/3/library/venv.html
# the above is the command for zsh

# now we can install packages in the venv
# Quick start guide
# https://flask.palletsprojects.com/en/2.2.x/quickstart/

# In terminal:
# export FLASK_APP=<filename>
# flask run
# it will automatically deploy at
# http://127.0.0.1:5000/
# which is the local server path
# make changes and re execute flask run
# don't want to have to restart the server
# every time we make a change. YOu will see
# that debug mode is off
# turn it on by executing
# export FLASK_ENV=development
# then it will say debugger is active
# the server will auto restart when you make changes

# flask converts text to html so the browser can understand it
# or you can use render_template to use your own html files

# static files are those which don;t change such as css and js files
# they live in a folder called static

# adding a favicon:
# https://flask.palletsprojects.com/en/1.1.x/patterns/favicon/
# <link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}">
# flask is a templating language where we can build stuff dynamically
# e.g., if we do {{ 4 + 5}} in our html file, flask
#  sees it as a python expression that needs to be evaluated as python
# it is good to build url instead of hardcoding (see flask docs)

# variable rules:
# enables us to create dynamic routes
# @app.route("/<username>")
# flask sees username as a variable it can pass into the 
# see the hello world function and index.html
# there are different rules, e.g., force integer, float 
# etc. See documentation under variable rules. Will get Not Found
# if breaking the rules



from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)
# print(__name__)

# decorator - gives extra server tools
# define a function every time we hit slash
@app.route("/<username>/<int:post_id>")
def hello_world(username=None, post_id=None):
    # render_template automatically looks 
    # in a folder called templates 
    return render_template('index.html',name=username, post_id=post_id)

@app.route("/about.html")
def about_me():
    # render_template automatically looks 
    # in a folder called templates 
    return render_template('about.html')

# found at server link/blog
@app.route("/blog/2020/dogs")
def blog2():
    return "This is my dog"
