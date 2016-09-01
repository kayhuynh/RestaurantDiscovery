from app import app, oauth
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

#For testing purposes
import sys 

@app.route('/')
def index():
	return "Hello world"

@app.route("/test")
def test_resp():
	print('Hello world!', file=sys.stderr)

	return redirect("/test")
