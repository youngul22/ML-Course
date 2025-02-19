import random

"""get computer input"""
def get_computer_choice():
    computer_choice = random.choice([1, 2, 3])

    if computer_choice == 1:
        print("Computer: 1. Rock")
    elif computer_choice == 2:
        print("Computer: 2. Paper")
    else:
        print("Computer: 3. Scissors")

    return computer_choice

"""get user input"""
def get_user_choice():
    print("Rock, Paper, Cissors - Let's play!")
    print("Enter your choice: ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    while True:
        try:
            user_choice = int(input("Enter your choice(1/2/3): "))
            if user_choice in [1, 2, 3]:
                break
            else:
                print("Invalid input. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number(1/2/3).")
    
    return user_choice

"""determine winner"""
def whowin(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 1 and computer == 3) or \
         (user == 2 and computer == 1) or \
         (user == 3 and computer == 2):
        return "You win!"
    else:
        return "You lose!"

"""Play Rock, Paper, Cissors with a user."""
def play():
    """User input"""
    user_choice = get_user_choice()

    """Computer input"""
    computer_choice = get_computer_choice()

    """Determine winnwer"""
    whowinmsg = whowin(user_choice, computer_choice)

    """Display winnwer"""
    print(whowinmsg)


if __name__ == "__main__":
    play()