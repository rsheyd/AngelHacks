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
	start = 'Tell me about how you are feeling'
 	return question (start)


@ask.intent("BadIntent")
def feeling_good():
	feeling_bad_resp = 'That sounds tough. What emotions are you feeling right now?'
	return statement(feeling_bad_resp)

@ask.intent("Intent4")
def find_emotion():
	emotion_q = 'How do you know you are feeling this way?'
	return statement(emotion_q)

@ask.intent("Intent5")
def sympathize():
	symp = 'Wow, that seems like a lot to deal with and I can imagine very difficult. Could you imagine things being different?'
	return statement(symp)

@ask.intent("Intent6")
def goal_set():
	goal = 'That is great! What is a specific goal you can mek that can imporve your situation?'
	return statement(goal)

@ask.intent("Intent7")
def goal_set_enviro():
	enviro = 'Identifying a goal is the first step. Next is knowing when you have achieved this goal. How do you know when your goals have been met? What will this look like?'
	return statement(enviro)

@ask.intent("Intent8")
def achievable():
	achieve = 'Do you think this is an achievable and realistic goal?'
	return statement(achieve)

@ask.intent("Intent9")
def goal_time():
	time = 'Great! Now that you have a specific, measurable and realistic goal, what is a realistic time frame to complete your goal?'
	return statement(time)


if __name__ == "__main__":
	app.run(debug=True)



