import random

class NumberGuesser:
    def __init__(self, min_num=1, max_num=10, max_guesses=4, max_hints=3):
        self.number = random.randint(min_num, max_num)
        self.max_guesses = max_guesses
        self.remaining_guesses = max_guesses
        self.max_hints = max_hints
        self.remaining_hints = max_hints
        self.min_num = min_num
        self.max_num = max_num
        self.hint_manager = NumberHint(self.number, self.min_num, self.max_num)

    def play(self):
        print(f"Welcome to Number Guesser! I have chosen a number between {self.min_num} and {self.max_num}.")
        print(f"You have {self.max_guesses} guesses. Type 'hint' for up to {self.max_hints} hints.")
        
        while self.remaining_guesses > 0:
            guess = input("Enter your guess: ")
            
            if guess.lower() == 'hint':
                print(self.hint_manager.get_hint(self.remaining_hints))
                if self.remaining_hints > 0:
                    self.remaining_hints -= 1
                print(f"Remaining hints: {self.remaining_hints}")
                continue
            
            if not guess.isdigit():
                print("Please enter a valid number.")
                continue
            
            guess = int(guess)
            
            if guess == self.number:
                print("Congratulations! You guessed the number correctly!")
                return
            else:
                self.remaining_guesses -= 1
                print("Wrong guess!")
                if self.remaining_guesses > 0:
                    print(f"Try again. You have {self.remaining_guesses} guesses left.")
                
        print(f"Game over! The correct number was {self.number}.")

class NumberhiHint:
    def __init__(self, number, min_num, max_num):
        self.number = number
        self.min_num = min_num
        self.max_num = max_num
        self._calculate_properties()

    def _calculate_properties(self):
        self.factors = [i for i in range(1, self.number + 1) if self.number % i == 0]
        self.multiples = [self.number * i for i in range(1, 4) if self.number * i <= self.max_num]
        self.parity = f"The number is {'even' if self.number % 2 == 0 else 'odd'}."
        self.larger_hint = f"The number is larger than {random.randint(self.min_num, self.number - 1)}." if self.number > self.min_num else None
        self.smaller_hint = f"The number is smaller than {random.randint(self.number + 1, self.max_num)}." if self.number < self.max_num else None
        
        self.available_hints = {
            'factors': f"One factor of the number is {random.choice(self.factors)}." if self.factors else None,
            'multiples': f"One multiple of the number is {random.choice(self.multiples)}." if self.multiples else None,
            'parity': self.parity,
            'larger': self.larger_hint,
            'smaller': self.smaller_hint
        }
        
        self.available_hints = {k: v for k, v in self.available_hints.items() if v is not None}

    def get_hint(self, remaining_hints):
        if remaining_hints == 0:
            return "Sorry, you've used all your hints!"
        
        if not self.available_hints:
            return "No more unique hints available!"
        
        chosen_hint = random.choice(list(self.available_hints.keys()))
        hint_message = self.available_hints.pop(chosen_hint)
        
        return hint_message
    


def main():
    game = NumberGuesser(1, 15, 4, 4)
    game.play()

if __name__ == "__main__":
    main()
