from sklearn.linear_model import LinearRegression
from pyautogui import pymsgbox

train_input = []
train_output = []
ai_victory = 0
user_victory = 0
rounds = 1
valid_input = {"Rock" : 1, "Paper" : 2, "Scissors" : 3}
valid_output = {1 : "Rock", 2 : "Paper", 3 : "Scissors"}
victory_dict = {"Rock" : "Paper", "Paper" : "Scissors", "Scissors" : "Rock"}
last_response = "Rock"
secondTo_last_response = "Rock"
thirdTo_last_response = "Rock"
correct_aiResponse = "Paper"
predictor = LinearRegression(n_jobs=-1)

def run():
    global last_response
    global secondTo_last_response
    global correct_aiResponse
    global thirdTo_last_response
    global user_victory
    global ai_victory
    global rounds

    # Get player's input
    user_response = pymsgbox.confirm(text="Rock Paper Scissors?", title="Rock Paper Scissors", buttons=("Rock", "Paper", "Scissors"))
    
    # Place player's input into last response
    thirdTo_last_response = secondTo_last_response
    secondTo_last_response = last_response
    last_response = user_response

    # Get ai's prediction off of last 3 moves
    ai_responseRaw = logic(ConvertToInput(last_response), ConvertToInput(secondTo_last_response), ConvertToInput(thirdTo_last_response))
    ai_response = ConvertToOutput(ai_responseRaw)

    # Increment score based on who won
    victory_counter(user_response, ai_response)
    
    pymsgbox.alert(text="AI says: "+ai_response+"\n\nRound: "+str(rounds)+"\n\nScore:\nAI: "+str(ai_victory)+" Player: "+str(user_victory), title="Rock Paper Scissors")

    # Check ai's answer against the correct one
    correct_aiResponse = correct(user_response)

    # Train the model off of the last three moves
    train_input.append([ConvertToInput(last_response), ConvertToInput(secondTo_last_response), ConvertToInput(thirdTo_last_response)])
    train_output.append(ConvertToInput(correct_aiResponse))
    train_model(train_input, train_output)

    # Output round report to console
    print(f"\nround report: \nround: {rounds}\nai wins: {ai_victory}, player wins: {user_victory}\nlast response: {last_response}\nSecond to last response: {secondTo_last_response}\nThird to last response: {thirdTo_last_response}\nML training input (1 = Rock, 2 = Paper, 3 = Scissors): {train_input}\nML training output: {train_output}")

    # Winning cards
    #winning_cards(rounds, ai_victory, user_victory)

    rounds += 1

def train_model(x, y):
    global predictor
    predictor.fit(X=x, y=y)

def logic(data1, data2, data3):
    global predictor
    test =  [[data1, data2, data3]]
    outcome = predictor.predict(X=test)
    return outcome

def ConvertToInput(data):
    global valid_input
    return valid_input[str(data)]

def ConvertToOutput(data):
    global valid_output
    try:
        return valid_output[int(data)]
    except Exception as e:
        print(f"Error on line 77, {data} is not a valid key.  Exception caught: {e}")
        return valid_output[1]

def correct(user):
    global victory_dict
    return victory_dict[user]

def victory_counter(user, ai):
    global victory_dict
    global ai_victory
    global user_victory
    if user == ai:
        return
    elif victory_dict[user] != ai:
        user_victory += 1
    else:
        ai_victory += 1

def winning_cards(rounds, ai_victory, user_victory):
    score = 7
    if user_victory == score and ai_victory <= score:
        win = pymsgbox.alert(text="Rounds "+str(rounds)+"\nYour score: "+str(user_victory)+"\nAI's score: "+str(ai_victory)+"\nYou outsmarted a machine designed to predict your every move with pinpoint accuracy.  Color me impressed.", title="You Win!")
        exit()
    elif ai_victory == score and user_victory < score:
        lose = pymsgbox.alert(text="Rounds "+str(rounds)+"\nYour score: "+str(user_victory)+"\nAI's score: "+str(ai_victory)+"\nYou lost.  But don't feel bad.  This machine is designed to learn to predict your every move with pinpoint accuracy.  You hardly ever stood a chance.", title="You Lose!")
        exit()

train_input.append([ConvertToInput(last_response), ConvertToInput(secondTo_last_response), ConvertToInput(thirdTo_last_response)])
train_output.append(ConvertToInput(correct_aiResponse))
train_model(train_input, train_output)

while True:
    try:
        run()
    except Exception as e:
        print(f"\n{e}\nApplication terminating...")
        exit()