import random

def dice_roll_game():
    correct_answer = random.randint(1, 6)
    user_guess = int(input("აირსჩიე ნომერი 1-დან 6-ამდე: "))
    
    if user_guess == correct_answer:
        print("სწორია!")
    else:
        print(f"არასწორია, ნომერი იყო {correct_answer}.")

dice_roll_game()
