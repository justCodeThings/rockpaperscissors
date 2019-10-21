from sklearn.linear_model import LinearRegression
from pyautogui import pymsgbox

rounds = 1
valid_input = {1 : 1, 2 : 2, 3 : 3}
valid_output = {1 : "Rock", 2 : "Paper", 3 : "Scissors"}
victory_dict = {1 : 2, 2 : 3, 3 : 1}
ai_one_response = 0
ai_two_response = 0
ai_one_correct_response = 0
ai_two_correct_response = 0
ai_one_outcome = 0
ai_two_outcome = 0
ai_one_last_responses = [1, 1, 1 ]
ai_two_last_responses = [1, 1, 1 ]
ai_one_train_input = []
ai_two_train_input = []
ai_one_train_output = []
ai_two_train_output = []
ai_one_victory = 0
ai_two_victory = 0
ai_one_answer = 0
ai_two_answer = 0

ai_one_predictor = LinearRegression(n_jobs=-1)
ai_two_predictor = LinearRegression(n_jobs=-1)

class ai(object):
    '''How to use: Initialize the ai class and pass it the opponents response (it will need a fake response to get
    started), the last reponses of the opponents in a list(again, the ai will need three fake previous response), the 
    training input list and the training output list. Exchange move with the think and log_response methods,
    than self correct and train the model and exchange again.'''
    def __init__(self, last_responses, own_response, correct_response, training_input, training_output, predictor):
        self.last_responses = last_responses
        self.own_response = own_response
        self.correct_response = correct_response
        self.training_input = training_input
        self.training_output = training_output
        self.predictor = predictor
    def log_response(self, opponent_response):
        self.last_responses.append(opponent_response)
        self.last_responses.remove(self.last_responses[0])
    def think(self):
        own_responseRaw = self.logic(self.last_responses[2], self.last_responses[1], self.last_responses[0])
        self.own_response = Clean(own_responseRaw)
        return self.own_response
    def self_correct(self):
        self.correct_response = victory_dict[self.own_response]
    def train(self):
        self.training_input.append([self.last_responses[0], self.last_responses[1], self.last_responses[2]])
        self.training_output.append(self.correct_response)
        self.train_model(self.training_input, self.training_output)
    def train_model(self, x, y):
        self.predictor.fit(X=x, y=y)

    def logic(self, data1, data2, data3):
        self.predictor
        test =  [[data1, data2, data3]]
        outcome = self.predictor.predict(X=test)
        return outcome

def Clean(data):
    global valid_input
    try:
        return valid_input[int(data)]
    except Exception as e:
        return valid_input[1]

def ConvertToInput(data):
    global valid_input
    return valid_input[str(data)]

def ConvertToOutput(data):
    global valid_output
    try:
        return valid_output[int(data)]
    except Exception as e:
        return valid_output[1]

def victory_counter(user, ai):
    global victory_dict
    global ai_one_victory
    global ai_two_victory
    if user == ai:
        return
    elif victory_dict[user] != ai:
        user_victory += 1
    else:
        ai_victory += 1

ai_one = ai(ai_two_last_responses, ai_one_response, ai_one_correct_response, ai_one_train_input, ai_one_train_output, ai_one_predictor)
ai_two = ai(ai_one_last_responses, ai_two_response, ai_two_correct_response, ai_two_train_input, ai_two_train_output, ai_two_predictor)

ai_one.train()
ai_two.train()

ai_one.log_response(1)
ai_one_answer = ai_one.think()
while True:
    ai_two.log_response(ai_one_answer)
    ai_two_answer = ai_two.think()
    ai_one.log_response(ai_two_answer)
    ai_one.self_correct()
    ai_two.self_correct()
    ai_one.train()
    ai_two.train()
    ai_one_answer = ai_one.think()
    print(f"AI one: {ConvertToOutput(ai_one_answer)}, AI two: {ConvertToOutput(ai_two_answer)}.\n\n")
    '''except Exception as e:
        print(f"\n{e}\nApplication terminating...")
        exit()'''