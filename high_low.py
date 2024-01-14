from art import logo
from art import vs
from game_data import data
import random
import os #os.system('cls')

data2 = data.copy()

def play():
    live = True
    score = 0

    #Choosing first contender and removing it from the list
    numberA = random.randint(0,len(data)-1)
    first_choice = data[numberA]
    nameA = first_choice["name"]
    descA = first_choice["description"]
    countryA = first_choice["country"]
    followerA = first_choice["follower_count"]
    data.pop(numberA)
    
    #Function to compare the 2 contenders
    def answering(follA,follB):
        answer = input("Who's has more followers? Type 'A or 'B': ").lower()
        if answer == "a":
            if follA > follB: 
                return 1
            else:
                return False
        elif answer == "b":
            if follB > follA:
                return 1
            else:
                return False
        else:
            print("Choose A or B.")
            answering(followerA, followerB)
    
    #Game loop
    while live:

        #Choosing second contender and removing it from the list
        numberB = random.randint(0,len(data)-1)
        second_choice = data[numberB]
        nameB = second_choice["name"]
        descB = second_choice["description"]
        countryB = second_choice["country"]
        followerB = second_choice["follower_count"]
        data.pop(numberB)
        
        #User interface
        os.system('cls')
        print(logo)
        print(f"Your score is: {score}")
        print(f"Compare A: {nameA}, a {descA}, from {countryA}")
        print(vs)
        print(f"Against B: {nameB}, a {descB}, from {countryB}")
        
        #checking if the list is clear
        if not data:
            if input(f"{nameA} has {followerA} and {nameB} has {followerB}\nYour score is {score}. You got it all!\nPlay again? Y or N: ").lower() == "y":
                data.clear()
                data.extend(data2)
                play()
            else:
                print("Thanks for playing!")
            live = False
        
        #checking win loose
        if answering(followerA, followerB) == False: #GameOver
            if input(f"Sorry, that's wrong. {nameA} has {followerA} and {nameB} has {followerB}\nFinal score: {score}\nPlay again? Y or N: ").lower() == "y":
                data.clear()
                data.extend(data2)
                play()
            else:
                print("Thanks for playing!")
            live = False
        else:
            input(f"You won! {nameA} has {followerA} and {nameB} has {followerB}\nPress enter to continue: ")
            score += 1
            if followerB > followerA:
                first_choice = second_choice
                nameA = first_choice["name"]
                descA = first_choice["description"]
                countryA = first_choice["country"]
                followerA = first_choice["follower_count"]

        
play()
