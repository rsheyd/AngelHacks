from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode

app = Flask (__name__)
ask = Ask(app, "/skill")
goalTries = 1

@app.route('/')
def homepage():
	return "Hi there, how ya doin?"

@ask.launch
def start_skill():
	start = "What's going on for you today?"
 	return question(start)

@ask.intent("NegativeFeelingResponse")
def find_emotion(feeling):
    sympathy = "Wow, that seems like a lot to deal with and I can \
            imagine it's very difficult. Could you imagine things \
            being different?"
    return question(sympathy)

@ask.intent("FeelingExplanationResponse")
def sympathize():
	symp = "That sounds tough. What emotions are you feeling right now?"
	return question(symp)

@ask.intent("PotentialActionResponse")
def goal_set():
	goal = 'That is great! What is a specific goal you can make \
            that can improve your situation?'
	return question(goal)

@ask.intent("GoalResponse")
def goal_set_enviro():
	enviro = 'Identifying a goal is the first step. Next is knowing \
              when you have achieved this goal. What will this look like?'
	return question(enviro)

@ask.intent("QualifyGoalResponse")
def achievable():
	achieve = 'Do you think that this is an achievable, and realistic, goal?'
	return question(achieve)

@ask.intent("YesIntent")
def goal_time():
    global goalTries
    goalTries = 1
    time = 'Awesome! Now that you have a specific, measurable and realistic \
            goal, what is a specific timeframe to complete your goal?'
    return question(time)

@ask.intent("NoIntent")
def ask_new_goal():
    global goalTries
    if goalTries > 2:
        goalTries = 1
        return statement("It can be tough to set a realistic goal. \
            Sometimes it helps me to take a walk or listen to music \
            to get a new perspective. Let's try again later.")
    else:
        goalTries = goalTries + 1
        return question("That's okay. Tell me another action that \
            may be more realistic.")        

@ask.intent("DateTargetSet")
def finish(datetime):
    ending = 'Great. I will follow up with you on {} evening. Good luck!' \
            .format(datetime)
    return statement(ending)

if __name__ == "__main__":
	app.run(debug=True)



