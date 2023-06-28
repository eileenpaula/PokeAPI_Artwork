from flask import Flask as fl
import requests
import openai
import json
import os


url = "https://pokeapi.co/api/v2/pokemon/"
error = "Invalid Pokemon name!"
valid_name = False

print("Generate artwork based off of a Pokemon of your choosing!")
print("Enter the name of a pokemon or enter exit to close the program.")
while valid_name is False:
    pokemon_name = input("Please enter the name of a Pokemon in all lowercase: ")
    if len(pokemon_name) == 0:
        print(error + " Name cannot be empty.")
        continue
    elif pokemon_name == "exit":
        break
    try:
        response = requests.get(url + pokemon_name).json()
    except:
        print(error + " Pokemon " + pokemon_name + " not found.")
    else:
        valid_name = True



print(response)
