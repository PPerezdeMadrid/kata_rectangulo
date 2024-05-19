import bowlinggame
import unittest

class KataBowling2(unittest.TestCase):
    
    def setUp(self):
        self.game = bowlinggame.Game()    
        
    def test_valid_game_rounds(self):
        for i in range(11):
            self.game.play_a_round()
            
        played_rounds = self.game.count_rounds()
        self.assertTrue(10, played_rounds)
        
    def test_regular_round(self): # a regular round has two attempts 
        for i in range(11):
            self.game.play_a_round()
            
        played_attempts = self.game.check_attempts(10, False)
        self.assertEqual(2, played_attempts)
        
    def test_extra_round(self): # the 10th round may have or may not a third attempt
        for i in range(11):
            self.game.play_a_round()
           
        played_attempts = self.game.check_attempts(10, True)
        self.assertEqual(3, played_attempts)
    
    def test_scored_points_per_attemps(self):
        pins_dropped = self.game.roll_a_ball()
        self.assertTrue(0 <= pins_dropped <= 10)
    
    def test_open_frame(self):
        type_of_point = self.game.points_clasifier([1,6], 1)
        self.assertEqual('open frame', type_of_point)
        
    def test_strike(self):
        type_of_point = self.game.points_clasifier([10, 0], 5)
        self.assertEqual('strike', type_of_point)
        
    def test_spare(self):
        type_of_point = self.game.points_clasifier([4,6], 3)
        self.assertEqual('spare', type_of_point)
        
    def test_count_simple_points(self): #A simple point is one that is earned by adding just points (no spare nor strikes)
        points_on_round_two = self.game.calculate_points([[1,6], 1], [[5,2], 2])
        self.assertEqual(14, points_on_round_two)

    def test_check_scoreboad(self):
        self.game.play_a_round(6,3)
        self.game.play_a_round(3,4)
        self.game.play_a_round(4,3)
        board = self.game.consult_scoreboard()
        self.assertEqual([9,16,23], board)
        
    # def test_count_strike_points(self):
    #     self.game.play_a_round(10,0)
    #     self.game.play_a_round(6,2)
    #     self.game.play_a_round(1,7)
    #     board = self.game.consult_scoreboard()
    #     self.assertEqual([18, 25, 33], board)

    # def test_count_spare_points(self):
    #     self.game.play_a_round(6,4)
    #     self.game.play_a_round(3,4)
    #     board = self.game.consult_scoreboard()
    #     self.assertEqual([10,17], board)
    
if __name__ == "__main__":
    unittest.main()