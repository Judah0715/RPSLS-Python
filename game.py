from human import Human
from ai import Ai
from player import Player


class Game():
    def __init__(self):
        pass


    def welcome(self):
        print("Welcome to a classic game with a little twist")
        print('Each player picks a gesture and reveals it at the same time. The winner is the one who gets 2 wins. In a tie, the process is repeated until a winner is found.')
        print('You can choose between Rock, Paper, Scissors, Lizard or Spock')
        print('Rock crushes Scissors')
        print('Scissors cuts Paper')
        print('Paper covers Rock')
        print('Rock crushes Lizard')
        print('Lizard poisons Spock')
        print('Spock smashes Scissors')
        print('Scissors decapitates Lizard')
        print('Lizard eats Paper')
        print('Paper disproves Spock')
        print('Spock vaporizes Rock')


        def run_game(self):
            self.welcome()
            self.game_select()
            while (self.player_one.player_score < 2 and self.player_two.player_score <2):
                self.player_one.choose_gesture()
                self.player_two.choose_gesture()
                self.compare_gestures()
                self.display_winner()


        def display_winner(self):
            if (self.player_one.player_score == 2):
                print(f"{self.player_one.name} wins the game!")

            elif (self.player_two.player_score ==2):
                print(f"{self.player_two.name} wins the game!")

                
