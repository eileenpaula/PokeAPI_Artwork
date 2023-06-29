from flask import Flask, redirect, render_template, request, url_for
import requests
import openai
import json
import os
import openai


def generate_art():
    openai.api_key = "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"
    url = "https://pokeapi.co/api/v2/pokemon/"
    error = "Invalid Pokemon name!"

    valid_name = False
    print("Generate pokemon art using openAI's API.")
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
            print(error + " Pokemon " + pokemon_name + " not found." )
        else:             
            valid_name = True 
    
    desc = "Generate a fully colored, realistic art piece with a colorful background based on the following:\n\nPokemon: " + pokemon_name + "\nDescription:\n"
    desc += requests.get(response["species"]["url"]).json()["flavor_text_entries"][0]["flavor_text"]

    response = openai.Image.create(
    prompt=desc,
    n=1,
    size="1024x1024"
    )
    image_url = response['data'][0]['url']

    print("The following URL contains the generated artwork:\n")
    return image_url

print(generate_art())