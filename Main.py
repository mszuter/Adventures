# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 10:53:29 2018

@author: sicher
"""
import json

def profile(character):
    name = character['Name']
    if character['Strength'] < 20:
        strength_desc = "very weak"
    elif character['Strength'] < 40:
        strength_desc = "weak"
    elif character['Strength'] < 60:
        strength_desc = "of average strength"
    elif character['Strength'] < 80:
        strength_desc = "strong"
    else:
        strength_desc = "very strong"
    print("This person's name is {0:}, they are {1:}".format(name, strength_desc))

def save_base_char(character):
    save_name = character['Name']
    with open(character['Name'] + ".sav", 'w') as save_file:
        save_file.write(json.dumps(character))
    print("New character saved!")
    
    

def new_game():
    name = input("Please enter the name of your character:")
    print("You have 100 attribute points to choose from. You will not be able to change these attributes during the game. Please choose carefully.")
    strength = int(input("Choose an amount to apply to innate strength (affects how strong you can become and how quickly you gain strength):"))
    intelligence = int(input("Choose an amount to apply to intelligence (affects how much knowledge you can gain and how quickly you learn):"))
    build = int(input("Choose an amount to apply to build (affects how flexible you are and how quickly you can move--higher build = more flexible and faster):"))
    charm = int(input("Choose an amount to apply to charm (affects how quickly you build rapport and how fast you learn new social skills):"))
    new_char = {"Name": name, "Strength" : strength, "Intelligence" : intelligence, "Build" : build, "Charm" : charm}
    save_base_char(new_char)
    profile(new_char)

def open_screen():
    print("Welcome to your adventure")
    print("1) New game")
    print("2) Load game")
    choice = int(input("Which option do you choose?"))
    rep = True
    print(choice)
    while rep == True:
        if choice == 1:
            new_game()
            rep = False
        elif choice == 2:
            load_game()
            rep = False
        else:
            rep = True

def load_game():
    char_name = input("Please enter the character name")
    with open(char_name + ".sav", 'r') as load_file:
        temp_char = json.load(load_file)
    profile(temp_char)
    
    

open_screen()