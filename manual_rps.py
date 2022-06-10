import random

class RockPaperScissorsGame:

    def __init__(self):
        self.number_of_wins = 0
        self.number_of_losses = 0
        self.number_of_ties = 0
        self.possible_selections = {'rock': 0, 'paper': 1, 'scissors': 2}
        print("Welcome to the Rock, Paper, Scissors Game")
        print("The rules of the game are: Rock smashes scissors, scissors cuts paper and paper covers rock")

    def get_computer_choice(self):
        return random.choice(list(self.possible_selections.keys()))

    def get_user_choice(self):
        return input("Please enter a choice (rock, paper or scissors): ").lower()

    def get_winner(self, user_choice, computer_choice):
        outcome = (user_choice - computer_choice) % 3
        if outcome == 0:
            self.number_of_ties += 1
            print("It's a tie -")
        elif outcome == 1:
            self.number_of_wins += 1
            print("You win!!!")
        elif outcome == 2:
            self.number_of_losses += 1
            print("You lose...")
    
    def scoreboard(self):
        print(f"You have {self.number_of_wins} wins, {self.number_of_losses} losses, and "
              f"{self.number_of_ties} ties.")

    def play(self):
        while True:
            user_choice = self.get_user_choice()
            if user_choice not in self.possible_selections.keys():
                print("Invalid input, try again!")
            else:
                break
        computer_choice = random.choice(list(self.possible_selections.keys()))
        print(f"You've picked {user_choice}, and the computer picked {computer_choice}.")
        self.get_winner(self.possible_selections[user_choice], self.possible_selections[computer_choice])

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    while True:
        game.play()
        game.scoreboard()

        while True:

            play_again = input('Do you wish to play again? (y/n): ').lower()
            if play_again == 'n':
                print("Game Over!")
                exit()
            elif play_again == 'y':
                break
            else:
                print("Invalid input!\n")
                continue
