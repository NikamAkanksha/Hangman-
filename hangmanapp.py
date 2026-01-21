import random
import os
from collections import defaultdict

# Larger word list with categories
WORDS = {
    "animals": ["elephant", "kangaroo", "cheetah", "penguin", "octopus"],
    "fruits": ["pineapple", "strawberry", "blueberry", "mango", "kiwi"],
    "tech": ["python", "computer", "algorithm", "database", "internet"],
    "sports": ["football", "basketball", "tennis", "swimming", "golf"],
    "cities": ["mumbai", "delhi", "pune", "bangalore", "chennai"]
}

# ASCII art stages (0-6 wrong guesses)
HANGMAN_ART = [
    """
     _____
    |     |
          |
          |
          |
          |
    =========
    """,
    """
     _____
    |     |
    O     |
          |
          |
          |
    =========
    """,
    """
     _____
    |     |
    O     |
    |     |
          |
          |
    =========
    """,
    """
     _____
    |     |
    O     |
   /|     |
          |
          |
    =========
    """,
    """
     _____
    |     |
    O     |
   /|\\    |
          |
          |
    =========
    """,
    """
     _____
    |     |
    O     |
   /|\\    |
   /      |
          |
    =========
    """,
    """
     _____
    |     |
    O     |
   /|\\    |
   / \\    |
          |
    =========
    """
]

class AdvancedHangman:
    def __init__(self):
        self.secret_word = ""
        self.category = ""
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.max_wrong = 6
        self.score = 0
        self.games_played = 0
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def select_word(self):
        category = random.choice(list(WORDS.keys()))
        self.secret_word = random.choice(WORDS[category]).upper()
        self.category = category.upper()
        self.guessed_letters.clear()
        self.wrong_guesses = 0
        return category
    
    def display_word(self):
        display = []
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display.append(letter)
            else:
                display.append("_")
        return " ".join(display)
    
    def get_stats(self):
        letters_left = self.secret_word.count('_')
        return {
            'length': len(self.secret_word),
            'letters_left': letters_left,
            'guessed': len(self.guessed_letters),
            'wrong': self.wrong_guesses,
            'hint_cost': max(1, letters_left // 2)
        }
    
    def draw_hangman(self):
        print(HANGMAN_ART[self.wrong_guesses])
    
    def show_board(self):
        self.clear_screen()
        self.draw_hangman()
        print(f"\n🏆 Score: {self.score} | Game #{self.games_played}")
        print(f"📂 Category: {self.category}")
        print(f"🎯 Word: {self.display_word()}")
        print(f"📝 Guessed: {', '.join(sorted(self.guessed_letters)) or 'None'}")
        print(f"❌ Wrong: {self.wrong_guesses}/{self.max_wrong}")
        stats = self.get_stats()
        print(f"📊 Letters left: {stats['letters_left']}/{stats['length']}")
    
    def give_hint(self):
        unguessed = set(self.secret_word) - self.guessed_letters
        if unguessed:
            hint_letter = random.choice(list(unguessed))
            self.guessed_letters.add(hint_letter)
            return f"💡 Hint: '{hint_letter}' was revealed!"
        return "No hints left!"
    
    def play(self):
        self.games_played += 1
        
        category = self.select_word()
        print(f"\n🎮 New game! Category: {category}")
        input("Press Enter to start...")
        
        while self.wrong_guesses < self.max_wrong:
            self.show_board()
            
            if "_" not in self.display_word():
                self.score += 100 - (self.wrong_guesses * 10)
                self.show_board()
                print("🎉 CONGRATULATIONS! You won!")
                print(f"💰 Score this game: {100 - (self.wrong_guesses * 10)}")
                input("\nPress Enter for next game...")
                return True
            
            print("\nCommands: [letter], 'h' = hint, 'q' = quit")
            guess = input("Your guess: ").strip().upper()
            
            if guess.lower() == 'q':
                print("👋 Thanks for playing!")
                return False
            elif guess.lower() == 'h':
                print(self.give_hint())
                input("Press Enter...")
                continue
            elif len(guess) != 1 or not guess.isalpha():
                print("❌ Enter single letter or 'h' for hint!")
                input("Press Enter...")
                continue
            elif guess in self.guessed_letters:
                print("✅ Already guessed!")
                input("Press Enter...")
                continue
            
            self.guessed_letters.add(guess)
            
            if guess not in self.secret_word:
                self.wrong_guesses += 1
                print("❌ Wrong guess!")
            else:
                print("✅ Correct!")
            
            input("Press Enter...")
        
        # Game over
        self.show_board()
        print(f"💀 Game Over! Word was: {self.secret_word}")
        print(f"📊 Final Score: {self.score}")
        input("\nPress Enter for next game...")
        return True

def main():
    game = AdvancedHangman()
    print("🎯 ADVANCED HANGMAN GAME")
    print("Multiple categories, hints, scoring, ASCII art!")
    
    while game.play():
        pass
    
    print(f"\n🏆 FINAL SCORE: {game.score}")
    print("Thanks for playing Advanced Hangman!")

if __name__ == "__main__":
    main()
