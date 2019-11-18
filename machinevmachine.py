
from time import sleep, time
import random

rounds = 1
valid_input = {1 : 1, 2 : 2, 3 : 3}
valid_output = {1 : "Rock", 2 : "Paper", 3 : "Scissors"}
ai_one_response = 0
ai_two_response = 0
ai_one_outcome = 0
ai_two_outcome = 0
ai_one_last_responses = [random.randint(1,3), random.randint(1,3), random.randint(1,3)]
ai_two_last_responses = [random.randint(1,3), random.randint(1,3), random.randint(1,3)]
ai_one_train_input = []
ai_two_train_input = []
ai_one_train_output = []
ai_two_train_output = []
ai_one_victory = 0
ai_two_victory = 0
ai_one_answer = random.randint(1,3)
ai_two_answer = random.randint(1,3)
ai_one_correct_response = victory_dict[ai_two_answer]
ai_two_correct_response = victory_dict[ai_one_answer]

ai_one_predictor = LinearRegression(n_jobs=-1)
ai_two_predictor = LinearRegression(n_jobs=-1)



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

def victory_counter(ai1, ai2):
    global victory_dict
    global ai_one_victory
    global ai_two_victory
    if ai1 == ai2:
        return
    if victory_dict[ai1] != ai2:
        ai_one_victory += 1
    if victory_dict[ai2] != ai1:
        ai_two_victory += 1

ai_one = Ai(ai_two_last_responses, ai_one_response, ai_one_correct_response, ai_one_train_input, ai_one_train_output, ai_one_predictor)
ai_two = Ai(ai_one_last_responses, ai_two_response, ai_two_correct_response, ai_two_train_input, ai_two_train_output, ai_two_predictor)

ai_one.train()
ai_two.train()
while True:
    now = time()
    ai_one_answer = ai_one.think()
    ai_two_answer = ai_two.think()
    ai_one.log_answer(ai_two_answer)
    ai_two.log_answer(ai_one_answer)
    victory_counter(ai_one_answer, ai_two_answer)
    print(f"Round: {rounds}, Score: {ai_one_victory} / {ai_two_victory} \nPlay: Bill= {ConvertToOutput(ai_one_answer)}, Ted= {ConvertToOutput(ai_two_answer)}.\nTime: {time()-now}.\n\n")
    rounds = rounds + 1
    #sleep(3)