import random

class Riddle:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class Character:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def increase_score(self):
        self.score += 1

class Scene:
    def __init__(self, description):
        self.description = description

class Game:
    def __init__(self):
        self.character = None
        self.scenes = []
        self.riddles = []
        self.load_riddles()
        self.load_scenes()

    def load_riddles(self):
        # Load riddles into the game
        self.riddles = [
            Riddle("I can be broken, but I’m not a physical object. What am I?", "A promise"),
            Riddle("The more you share me, the more I grow. What am I?", "Knowledge"),
            Riddle("What can be given away freely but, when hoarded, becomes a burden?", "Love"),
            Riddle("I can teach you, but I can also mislead you. What am I?", "Experience"),
            Riddle("I am often hidden in plain sight; I grow in the heart and flourish in the mind. What am I?", "Compassion"),
        ]

    def load_scenes(self):
        # Load narrative scenes into the game
        self.scenes = [
            Scene("Vikram, the brave king of Ujjain, stands at the entrance of the forest, where the spirit Vetal awaits."),
            Scene("Vetal appears, challenging Vikram with a riddle to test his wisdom and bravery."),
            Scene("After solving the riddle, Vikram gains insight and continues his quest deeper into the forest."),
            Scene("The forest holds many secrets, and Vikram must choose wisely to uncover them."),
            Scene("With each riddle solved, Vikram inches closer to understanding the true nature of wisdom."),
            Scene("Vikram faces the final challenge, where his choices will determine his fate.")
        ]

    def start(self):
        # Start the game
        player_name = input("Enter your name, brave warrior: ")
        self.character = Character(player_name)
        print(f"\nWelcome to Vikram's Quest, {self.character.name}!")

        self.play_game()

    def play_game(self):
        # Play the game scene by scene
        for scene in self.scenes:
            print(f"\n{scene.description}")
            if self.riddles:
                riddle = random.choice(self.riddles)
                self.riddles.remove(riddle)
                print(f"\nVetal asks: {riddle.question}")

                answer = input("Your answer: ")
                if answer.lower() == riddle.answer.lower():
                    print("Correct! Well done.")
                    self.character.increase_score()
                else:
                    print(f"Wrong! The correct answer was: {riddle.answer}")
            else:
                print("\nVetal has no more riddles to offer. You have proven your wisdom!")

        print(f"\nGame over, {self.character.name}! Your final score: {self.character.score}")

# Run the game
if __name__ == "__main__":
    game = Game()
    game.start()
