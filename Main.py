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
    
    if character['Knowledge'] < 20:
        knowledge_desc = "very uneducated"
    elif character['Knowledge'] < 40:
        knowledge_desc = "uneducated"
    elif character['Knowledge'] < 60:
        knowledge_desc = "moderately educated"
    elif character['Knowledge'] < 80:
        knowledge_desc = "educated"
    else:
        knowledge_desc = "very educated"
        
    if character['Flexibility'] < 20:
        flex_desc = "very stiff"
    elif character['Flexibility'] < 40:
        flex_desc = "stiff"
    elif character['Flexibility'] < 60:
        flex_desc = "of average flexibility"
    elif character['Flexibility'] < 80:
        flex_desc = "flexible"
    else:
        flex_desc = "very flexible"
        
    if character['Social skills'] < 20:
        social_desc = "very unfriendly"
    elif character['Social skills'] < 40:
        social_desc = "unfriendly"
    elif character['Social skills'] < 60:
        social_desc = "amiable"
    elif character['Social skills'] < 80:
        social_desc = "friendly"
    else:
        social_desc = "very friendly"    
    print("This person's name is {0:}, they are {1:}, {2:}, {3:}, and {4:}".format(name, strength_desc, knowledge_desc, flex_desc, social_desc))

def save_base_char(character):
    save_name = character['Name']
    with open(character['Name'] + ".sav", 'w') as save_file:
        save_file.write(json.dumps(character))
    print("New character saved!")
    
    

def new_game():
    name = input("Please enter the name of your character:")
    print("You have 100 attribute points to choose from. You will not be able to change these attributes during the game. Please choose carefully.")
    innate_strength = int(input("Choose an amount to apply to innate strength (affects how strong you can become and how quickly you gain strength):"))
    intelligence = int(input("Choose an amount to apply to intelligence (affects how much knowledge you can gain and how quickly you learn):"))
    build = int(input("Choose an amount to apply to build (affects how flexible you are and how quickly you can move--higher build = more flexible and faster):"))
    charm = int(input("Choose an amount to apply to charm (affects how quickly you build rapport and how fast you learn new social skills):"))
    new_char = {"Name": name, "Innate strength" : innate_strength, "Intelligence" : intelligence, "Build" : build, "Charm" : charm, "Carrying capacity" : 2, "Strength" : 1, "Knowledge" : 1, "Flexibility" : 1, "Social skills" : 1}
    save_base_char(new_char)
    new_inventory = ["bread"]
    save_inventory(new_char, new_inventory)
    profile(new_char)
    return(new_char, new_inventory)

def open_screen():
    print("Welcome to your adventure")
    print("1) New game")
    print("2) Load game")
    choice = int(input("Which option do you choose?"))
    rep = True
    print(choice)
    while rep == True:
        if choice == 1:
            player, inventory = new_game()
            rep = False
            play_loop(player, inventory)
        elif choice == 2:
            player, inventory = load_game()
            rep = False
            play_loop(player, inventory)
        else:
            rep = True

def load_game():
    char_name = input("Please enter the character name")
    with open(char_name + ".sav", 'r') as load_file:
        temp_char = json.load(load_file)
    with open(char_name + ".inv", 'r') as inv_file:
        temp_inv = inv_file.read()
    profile(temp_char)
    return(temp_char, temp_inv)
    
def save_inventory(char, inventory):
    file_name = char['Name'] + ".inv"
    with open(file_name, 'w') as outfile:
        outfile.write(json.dumps(inventory))

def play_loop(player, inventory):
    print("1) Look at inventory")
    print("2) View profile")
    choice = input("Choose an action:")
    if choice == 1:
        view_inventory(inventory)
    elif choice == 2:
        profile(player)
    
def view_inventory(inventory):
    print("The following items are in your inventory:")
    

open_screen()