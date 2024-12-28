import random
import time

def delay_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

# Game starts
def start_game():
    print("Welcome to the Forest Survival Game!") 
    delay_print("You find yourself lost in a thick, mysterious forest. Your goal is to survive.")
    delay_print("Choose wisely, as each decision may bring you closer to your survival of way out or a danger that leads you to death \n")

    while True:
        delay_print("Your choices are:")
        delay_print("1. Search for food")
        delay_print("2. Find water source")
        delay_print("3. Look for shelter to stay for a while")
        delay_print("4. Climb a tree to survey the area")
        delay_print("5. Start a fire to stay warm")
        delay_print("6. Follow a distant sound")

        try:
            choice = int(input("What would you like to do? Enter your first choice > "))

            if choice == 1:
                search_for_food()
            elif choice == 2:
                find_water()
            elif choice == 3:
                look_for_shelter()
            elif choice == 4:
                climb_tree()
            elif choice == 5:
                start_fire()
            elif choice == 6:
                follow_sound()
            else:
                delay_print("Invalid choice. Please enter a number between 1 and 6.")

        except ValueError:
            delay_print("Please enter a valid number.")

        if game_ended:
            break

# Game ending section
game_ended = False

def end_game(success):
    global game_ended
    game_ended = True
    if success:
        delay_print("Congratulations! You have survived the forest adventure!")
    else:
        delay_print("Unfortunately, your choices led to your early death in the forest. Better luck next time!")

def search_for_food():
    delay_print("\nYou decide to search for food.")
    delay_print("After a while, you find some berries. They look edible, but you're not sure.")
    delay_print("1. Eat the berries")
    delay_print("2. Ignore the berries and keep looking")

    try:
        choice = int(input("What would you like to do? Enter your choice > "))
        if choice == 1:
# Random chance of safe or dangerous berries
            if random.choice([True, False]):
                delay_print("The berries were safe to eat. You feel energized!")
            else:
                delay_print("The berries were poisonous! You feel dizzy and collapse...")
                end_game(False)
        elif choice == 2:
            delay_print("You decide not to risk it and move on, but you're getting hungrier.")
        else:
            delay_print("Invalid choice. Moving on...")
    except ValueError:
        delay_print("Please enter a valid number.")

def find_water():
    delay_print("\nYou decide to search for water.")
    delay_print("After a long search, you find a small stream. The water looks clean.")
    delay_print("1. Drink the water")
    delay_print("2. Boil the water first")
    
    try:
        choice = int(input("What would you like to do? Enter your choice > "))
        if choice == 1:
            delay_print("You drink the water directly. It tastes fresh that it feels you energized.")
        elif choice == 2:
            delay_print("You remember your survival training and decide to boil the water first.")
            delay_print("After boiling, you drink the safe water and feel refreshed.")
        else:
            delay_print("Invalid choice. Moving on...")
    except ValueError:
        delay_print("Please enter a valid number.")

def look_for_shelter():
    delay_print("\nYou decide to look for shelter.")
    delay_print("After some searching, you find a cave.")
    delay_print("1. Enter the cave")
    delay_print("2. Find another place")

    try:
        choice = int(input("What would you like to do? Enter your choice > "))
        if choice == 1:
            delay_print("You enter the cave. It's dark and smells strange and scary.")
            if random.choice([True, False]):
                delay_print("Suddenly, a wild animal appears and attacks you!")
                end_game(False)
            else:
                delay_print("You find a safe spot in the cave and rest peacefully.")
        elif choice == 2:
            delay_print("You decide not to risk it and keep searching. You find a large tree that provides some shelter.")
        else:
            delay_print("Invalid choice. Moving on...")
    except ValueError:
        delay_print("Please enter a valid number.")

def climb_tree():
    delay_print("\nYou decide to climb a tree to get a better view.")
    delay_print("1. Climb carefully")
    delay_print("2. Rush up the tree")

    try:
        choice = int(input("What would you like to do? Enter your choice > "))
        if choice == 1:
            delay_print("You climb carefully and get a good view of the surroundings.")
            delay_print("You spot a clearing nearby, which could be a way out.")
            end_game(True)
        elif choice == 2:
            delay_print("In your haste, you slip and fall from the tree!")
            end_game(False)
        else:
            delay_print("Invalid choice. Moving on...")
    except ValueError:
        delay_print("Please enter a valid number.")

def start_fire():
    delay_print("\nYou decide to start a fire to keep warm.")
    delay_print("1. Use dry wood and rocks")
    delay_print("2. Try using damp wood")

    try:
        choice = int(input("What would you like to do? Enter your choice > "))
        if choice == 1:
            delay_print("You successfully start a fire. It keeps you warm and deters animals.")
        elif choice == 2:
            delay_print("The damp wood does not catch a fire, and you waste precious time.")
        else:
            delay_print("Invalid choice. Moving on...")
    except ValueError:
        delay_print("Please enter a valid number.")

def follow_sound():
    delay_print("\nYou decide to follow the distant sound.")
    delay_print("After walking a while, you realize it was the sound of a river.")
    delay_print("1. Approach the river carefully")
    delay_print("2. Rush towards the sound")

    try:
        choice = int(input("What would you like to do? Enter your choice > "))
        if choice == 1:
            delay_print("You carefully approach and find a safe path along the river. This might be a way out!")
            end_game(True)
        elif choice == 2:
            delay_print("You rush towards the river, but you slip on a muddy slope and fall in. You struggle to swim...")
            end_game(False)
        else:
            delay_print("Invalid choice. Moving on...")
    except ValueError:
        delay_print("Please enter a valid number.")

start_game()