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
 	return question(start)

@ask.intent("NegativeFeelingResponse")
def find_emotion():
	emotion_q = "How do you know you are feeling this way?"
	return question(emotion_q)

@ask.intent("FeelingExplanationResponse")
def sympathize():
	symp = 'Wow, that seems like a lot to deal with and I can \
            imagine very difficult. Could you imagine things \
            being different?'
	return question(symp)

@ask.intent("PotentialActionResponse")
def goal_set():
	goal = 'That is great! What is a specific goal you can make \
            that can imporve your situation?'
	return question(goal)

@ask.intent("GoalResponse")
def goal_set_enviro():
	enviro = 'Identifying a goal is the first step. Next is knowing \
              when you have achieved this goal. How do you know when \
              your goals have been met? What will this look like?'
	return question(enviro)

@ask.intent("QualifyGoalResponse")
def achievable():
	achieve = 'Do you think this is an achievable and realistic goal?'
	return question(achieve)

@ask.intent("GoalRealisticAnswer")
def goal_time():
	return question(time)

@ask.intent("DateTargetSet")
def finish():
    ending = 'Good job, and good luck!'
    return statement(ending)

if __name__ == "__main__":
	app.run(debug=True)



