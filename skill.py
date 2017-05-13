from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode

app = Flask (__name__)
ask = Ask(app, "/skill")

@app.route('/')
def homepage():
	return "Hi there, how ya doin?"

@ask.launch
def start_skill():
 	return question ()


@ask.intent("GoodIntent")
def feeling_good():
	feeling_good_resp = 'I am glad you are doing well today'
	return statement(feeling_good_resp)



if __name__ == "__main__":
	app.run(debug=True)



