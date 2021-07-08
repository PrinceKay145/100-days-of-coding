import random
from art import logo_higher_lower, vs
from gamedata import data
from replit import clear

count = 0


def game_person():
    """Return a data from bunch of given data"""
    person = random.choice(data)
    return person


def compare(answer, guess_A, guess_B):
    """Take input from the user and check if A is the answer or B"""
    if guess_A > guess_B and answer == "A":
        return True
    elif guess_B > guess_A and answer == "B":
        return True
    else:
        return False


# Print out the first one against the second one
print(logo_higher_lower)
player_A = game_person()
player_B = game_person()
correct_answer = True
while correct_answer:
    # Generate a random list from the given data
    print(f"Compare A: {player_A['name']}, a {player_A['description']}, from {player_A['country']}")
    print(vs)
    print(f"Against B: {player_B['name']}, a {player_B['description']}, from {player_B['country']}")

    # Give the user the opportunity to guess who has the bigger follower
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()

    # compare their answer with what we have
    guess_A = player_A['follower_count']
    guess_B = player_B['follower_count']
    compare(answer, guess_A, guess_B)
    # i need a loop that keep track of count
    new_player = {}
    if compare(answer, guess_A, guess_B) == True:
        count += 1
        clear()
        print(logo_higher_lower)
        print(f"You're right!. Current score: {count}")
        new_player = player_A
        player_A = player_B
        player_B = game_person()
    elif compare(answer, guess_A, guess_B) == False:
        clear()
        print(f"Sorry, that's wrong. Your final score is {count}")
        correct_answer = False


