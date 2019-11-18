from sklearn.linear_model import LinearRegression

# Set dictionary to calculate Rock Paper Scissors winning moves
victory_dict = {1 : 2, 2 : 3, 3 : 1}

class Ai(object):
    '''Use this class to create AI players to play Rock Paper Scissors.  Use the think method to process an opponents response.  
    Use the log method to record the opponents response.  A fake opponent_response and corresponding correct_response  and 
    last_responses will be need to get things going, it's suggested they be set to a random int between 1 and 3.'''
    def __init__(self, last_responses, own_response, correct_response, training_input, training_output, predictor):
        self.last_responses = last_responses
        self.own_response = own_response
        self.correct_response = correct_response
        self.training_input = training_input
        self.training_output = training_output
        self.predictor = predictor
    def log_answer(self, opponent_response):
        # Log opponent's response
        self.last_responses.append(opponent_response)
        self.last_responses.remove(self.last_responses[0])
        # Store the actual winning response to the opponent's move to use for learning
        self.correct_response = victory_dict[opponent_response]
        # Train the AI off of this round's opponent plays and own plays
        self.train()
    def think(self):
        # Generate a response based on logic
        own_responseRaw = self.logic(self.last_responses[2], self.last_responses[1], self.last_responses[0])
        self.own_response = Clean(own_responseRaw)
        # Make sure response is different than last 3 responses
        if self.last_responses[0] == self.own_response and self.last_responses[1] == self.own_response and self.last_responses[2] == self.own_response:
            self.own_response = random.randint(1,3)
        # Return AI's response to opponent
        return self.own_response
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