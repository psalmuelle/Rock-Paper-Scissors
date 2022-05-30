import random

# a list and a dict containing the letters and their meaning
possible_options = ["R", "P", "S"]
opt_meaning = {"R": "Rock", "P": "Paper", "S": "Scissors"}

# status message funtion
def message (status) :
    if status == "win":
        print("Congratulations! You win.")
    elif status == "lose":
        print("Oops! You lose.")


#loop to get started again when there is a tie
replay = True 
while replay:

    #User choice get inputted
    user_choice = input("Pick an option between \"R\", \"P\", and \"S\": ").capitalize()

    #if it does not match with possible_options, it runs into a while loop until it is correct
    while possible_options.count(user_choice) == 0:
        user_choice = input("User input not among options!\nPick an option between \"R\", \"P\", and \"S\": ").capitalize()

    #computer or cpu choice get selected with random()
    computer_choice = random.choice(possible_options)
   

    #prints player and cpu inputs
    print(f"Player ({opt_meaning.get(user_choice)}) : CPU ({opt_meaning.get(computer_choice)})")

    #Conditions to set the winner and looser of the game

    if user_choice == "R" and computer_choice == "S":
        message("win")
        replay = False

    elif user_choice == "S" and computer_choice == "R": 
        message("lose")
        replay = False

    elif user_choice == "P" and computer_choice== "R":
        message("win")
        replay = False

    elif user_choice == "R" and computer_choice== "P":
        message("lose")
        replay = False

    elif user_choice == "S" and computer_choice== "P":
        message("win")
        replay = False

    elif user_choice == "P" and computer_choice== "S":
        message("lose")
        replay = False
    else:
        print("There was a tie!")
        replay = True
    