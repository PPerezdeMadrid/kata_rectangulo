import random

class Game():
    
    def __init__(self):
        self.attempts = 0 
        self.bonus = False    
        self.scoreboard = []
        self.round = len(self.scoreboard)
        

    def play_a_round(self, pins_dropped_0 = None, pins_dropped_1 = None):
        self.attempts = 0 
        if self.round <= 10:
            for i in range(1):
                if pins_dropped_0 is None or pins_dropped_1 is None:
                    pins_dropped_0 = self.roll_a_ball() 
                    pins_dropped_1 = self.roll_a_ball() 
                points = self.calculate_points(pins_dropped_0, pins_dropped_1)
                if len(self.scoreboard) >= 1:
                    points += self.scoreboard[-1] 
                
                self.scoreboard.append(points)    
                self.attempts += 1 

    
    def count_rounds(self):
        return self.round
    
    def check_attempts(self, rounds, bonus):
        # if rounds == len(self.scoreboard) and len(self.scoreboard) == 10 and bonus:
        if bonus:
            return 3
        else: 
            return 2
    
    def roll_a_ball(self):
        pins_dropped =  random.randint(0, 10)
        return int(pins_dropped)
    
    def points_clasifier(self, pins_dropped, round):
        if pins_dropped[0] == 10:
            return 'strike'
        else: 
            result = pins_dropped[0] + pins_dropped[1]
            if result == 10:
                return 'spare'
            else: 
                return 'open frame'
                
    def calculate_points(self, round_0, round_1):
        if isinstance(round_0, list) and isinstance(round_1, list):
            if (round_0[1] + 1) != round_1[1]:
                return "Error; Selected rounds cannot be added"
            else:
                pins_dropped_round_one = round_0[0]
                pins_dropped_round_one = pins_dropped_round_one[0] + pins_dropped_round_one[1]
                pins_dropped_round_two = round_1[0]
                pins_dropped_round_two = pins_dropped_round_two[0] + pins_dropped_round_two[1]
                result = pins_dropped_round_one + pins_dropped_round_two
                return result
        else:      
            return round_0 + round_1
    
    def consult_scoreboard(self):
        return self.scoreboard