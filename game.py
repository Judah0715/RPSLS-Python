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

        def compare_gestures(self):

            if self.player_one.chosen_gesture == "rock":
                if self.player_two.chosen_gesture == "rock":
                    print("It is a tie.")

                elif self.player_two.chosen_gesture =="paper":
                    self.player_two.player_score += 1
                    print(f"paper covers rock {self.player_two.naem} wins") 

                elif self.player_two.chosen_gesture == 'scissors':
                    self.player_one.player_score += 1
                    print(f'rock crushes scissors {self.player_one.name} wins')
   
                elif self.player_two.chosen_gesture == 'lizard':
                    self.player_one.player_score += 1
                    print(f'rock crushes lizard {self.player_one.name} wins')
            
                elif self.player_two.chosen_gesture == 'spock':
                    self.player_two.player_score +=1
                    print(f'spock vaporizes rock {self.player_two.name} wins')  

            if self.player_one.chosen_gesture == 'paper':
                if self.player_two.chosen_gesture == "rock":
                    self.player_one.player_score += 1
                    print(f'paper covers rock {self.player_one.name} wins')
            
                elif self.player_two.chosen_gesture == 'paper':
                     print('Its a tie') 

                elif self.player_two.chosen_gesture == 'scissors':
                    self.player_two.player_score += 1
                    print(f'scissors cut paper {self.player_two.name} wins')

                elif self.player_two.chosen_gesture == 'lizard':
                    self.player_two.player_score += 1
                    print(f'lizard eats paper {self.player_two.name} wins')
            
                elif self.player_two.chosen_gesture == 'spock':
                    self.player_one.player_score += 1
                    print(f'paper disproves spock {self.player_one.name} wins')
        
            if self.player_one.chosen_gesture == 'scissors':
                if self.player_two.chosen_gesture == 'rock':
                    self.player_two.player_score += 1
                    print(f'rock crushes scissors {self.player_two.name} wins')
            
                elif self.player_two.chosen_gesture == 'scissors':
                    print('Its a tie') 

                elif self.player_two.chosen_gesture == 'paper':
                    self.player_one.player_score += 1
                    print(f'scissors cut paper {self.player_one.name} wins')

                elif self.player_two.chosen_gesture == 'lizard':
                    self.player_one.player_score += 1
                    print(f'scissors decapitates lizard {self.player_one.name} wins')
            
                elif self.player_two.chosen_gesture == 'spock':
                    self.player_two.player_score += 1
                    print(f'spock smashes scissors {self.player_two.name} wins')
        
            if self.player_one.chosen_gesture == 'lizard':
                if self.player_two.chosen_gesture == 'rock':
                    self.player_two.player_score += 1
                    print(f'rock crushes lizard {self.player_two.name} wins')
            
                elif self.player_two.chosen_gesture == 'lizard':
                     print('Its a tie') 

                elif self.player_two.chosen_gesture == 'scissors':
                    self.player_two.player_score += 1
                    print(f'scissors decapitates lizard {self.player_two.name} wins')

                elif self.player_two.chosen_gesture == 'paper':
                    self.player_one.player_score += 1
                    print(f'lizard eats paper {self.player_one.name} wins')
            
                elif self.player_two.chosen_gesture == 'spock':
                    self.player_one.player_score += 1
                    print(f'lizard poisons spock {self.player_one.name} wins')
        
            if self.player_one.chosen_gesture == 'spock':
                if self.player_two.chosen_gesture == 'rock':
                    self.player_one.player_score += 1
                    print(f'spock vaporizes rock {self.player_one.name} wins')
            
                elif self.player_two.chosen_gesture == 'spock':
                     print('Its a tie') 

                elif self.player_two.chosen_gesture == 'paper':
                    self.player_two.player_score += 1
                    print(f'paper disproves spock {self.player_two.name} wins')

                elif self.player_two.chosen_gesture == 'scissors':
                    self.player_one.player_score += 1
                    print(f'spock smashes scissors {self.player_one.name} wins')
            
                elif self.player_two.chosen_gesture == 'lizard':
                    self.player_two.player_score += 1
                    print(f'lizard poisons spock {self.player_two.name} wins')


        def game_select(self):
            print("Please select single press 1, or mulitplayer press 2")
            self.game_mode = input("")


            if self.game_mode == "1":
                print("You have selected singleplayer.")
                self.player_one = Human()
                self.player_two = Ai()


            elif self.game_mode == "2":
                print("You have selected Muliplayer")
                self.player_one = Human()
                self.player_two = Human()


            else:
                print("You have not selected a proper game mode")
                self.game_select()
                    

                                 
