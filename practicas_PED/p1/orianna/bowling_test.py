# import unittest
# import bowlinggame 

# class KataBowling(unittest.TestCase):
    
#     def setUp(self):
#        self.game = bowlinggame.Game()
    
    
#     def test_a_game_starts(self):
#         pass
    
#     def test_game_ends(self):
#         pass
    
    
#     #1.1 
#     def test_game_with_10_rounds(self):
#         self.assertEqual(self.game.get_rounds(), 10)
    
#     #1.2  
#     def test_valid_attempts_regular_rounds(self):
#         for round in range(1,10): #Remeber it goes between 1-9 
#             attempt_value = self.game.get_attempt_in_round(round)
#             self.assertTrue(0 <= attempt_value <= 2)
            
#     def test_valid_attempts_last_round(self):
#         attempt_value = self.game.get_attempt_in_round(10)
#         self.assertTrue(0 <= attempt_value <= 3)
              
#     def test_play_attempt(self):
#         self.game.play_an_attempt(round)
        
    
    
#     def test_update_attempts(self):
#         for round in range(1,10):
#             for attempt in range(1,3):
#                 updating_method = self.game.update_attempts(round, attempt)
#                 getting_value = self.game.rounds[round][0]
#                 self.assertEqual(updating_method, getting_value)

#     def test_update_attempts_final_round(self):
#         for attempt in range(1,4):
#             updating_method = self.game.update_attempts(10, attempt)
#             getting_value = self.game.rounds[10][0]
#             self.assertEqual(updating_method, getting_value)

    
#     # P. Calcular los puntos 
#     # -Trae el punto / Traer LOS puntos
#     # -Identificar el tipo de puntos
#     # -Calculador de strike
#     # -Calculador de strike en la última ronda
#     # -Calculador de spares
#     # -Calculador de openframes
    
#     # def test_get_points(self):
#     #     game = bowlinggame.Game() 
#     #     round = 1
#     #     points = game.get_total_points_per_round(round)
        
#     #     game.rounds[round][2]
        
#     # def test_openframes_points(self):
#     #     game = bowlinggame.Game() 
#     #     playing_round = 
#     #     if playing_round != 0:
#     #         previous_round = playing_round - 1     
#     #         previous_points = game.rounds[previous_round][2]
#     #         actual_points = game.calculate_total_points(type_of_point, previous_points, )
        

    
# if __name__ == "__main__":
#     unittest.main()