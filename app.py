from flask import Flask, render_template, request
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import json
import random

import sqlalchemy as db
from sqlalchemy import select, asc

import os
import openai
import requests


app = Flask(__name__)

openai.api_key = ""

# Creating Database and Table
engine = db.create_engine('sqlite:///data_base_name.sqlite') #Create data_base_name.sqlite automatically
connection = engine.connect()
metadata = db.MetaData()

emp = db.Table('emp', metadata,
              db.Column('pokemon', db.String()),
              db.Column('url', db.String(), nullable=False)
              )

metadata.create_all(engine) #Creates the table

#query = db.delete(emp)
#query = query.where(emp.columns.pokemon != "N/A")
#results = connection.execute(query)

def get_random_pokemon():
    # Make a GET request to retrieve a list of all Pokémon
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=1000')
    if response.status_code == 200:
        pokemon_list = response.json()['results']
        # Select a random Pokémon from the list
        random_pokemon = random.choice(pokemon_list)
        return random_pokemon['name']
    else:
        print('Error:', response.status_code)

@app.route('/', methods=['GET', 'POST'])
def index(): 
    m = ""
    user_input_class = "contact-container"
    img_class = "ia-container is-hidden"
    reset_class = "reset has-text-centered is-hidden"
    img_url1=""
    img_url2=""
    img_url3=""
    poke_search=""
    submit = True
    if request.method == 'POST':
        try: 
            if request.form['submit_button'] == 'Random':
                poke_search = get_random_pokemon()
                submit = False
                print(poke_search)
        except:
            poke_search = request.form.get('poke-input')
        poke_search = poke_search.lower() # ensures that user input in lowercase
        if submit and not poke_search: #this is where validation
            m = "Please enter a Pokemon name." #if the user doesn't type anything, this will tell them to do so.
        #elif any(char.isdigit(_) for char in poke_search):
        elif submit and not poke_search.isalpha():
            m = "Pokemon name should contain only letters. Try again." #if they type numbers, it will ask them to enter a name instead        
        else:
            try:
                response = requests.get("https://pokeapi.co/api/v2/pokemon/" + poke_search).json()
            except:
                m = "Pokemon not found."
            else:
                desc = "Generate a fully colored, realistic art piece with a colorful background based on the following:\n\nPokemon: " + poke_search + "\nDescription:\n"
                desc += requests.get(response["species"]["url"]).json()["flavor_text_entries"][0]["flavor_text"]
                response = openai.Image.create(
                    prompt=desc,
                    n=1,
                    size="1024x1024"
                    )
                image_url1 = response['data'][0]['url']
                response = openai.Image.create(
                    prompt=desc,
                    n=1,
                    size="1024x1024"
                    )
                image_url2 = response['data'][0]['url']
                response = openai.Image.create(
                    prompt=desc,
                    n=1,
                    size="1024x1024"
                    )
                image_url3 = response['data'][0]['url']

                user_input_class += " is-hidden"
                img_class = "ia-container"
                reset_class = "reset has-text-centered"
                img_url1 = image_url1
                img_url2 = image_url2
                img_url3 = image_url3

                with engine.connect() as connection:
                    data = {"pokemon":poke_search, "url":image_url1}
                    connection.execute(emp.insert(), data)
                    data = {"pokemon":poke_search, "url":image_url2}
                    connection.execute(emp.insert(), data)
                    data = {"pokemon":poke_search, "url":image_url3}
                    connection.execute(emp.insert(), data)
        
    with engine.connect() as connection:
        query = db.select(emp)
        query_result = connection.execute(query)
        rows = query_result.fetchall()

    pokemon_dict = {}
    for row in rows:
        val = row['pokemon']
        try:
            pokemon_dict[val] += 1
        except:
            pokemon_dict[val] = 1
                
    sorted_dict = sorted(pokemon_dict.items(), key=lambda x: x[1], reverse=True)
    top_five = sorted_dict[:5]

    return render_template('index.html', message = m, user_input_class = user_input_class, 
    img_class = img_class, reset_class = reset_class, img_url1 = img_url1, img_url2 = img_url2, 
    img_url3 = img_url3, top_five = top_five, name = poke_search)

@app.route('/testing', methods=['GET', 'POST'])
def testing(): 
    with engine.connect() as connection:
        query = db.select(emp)
        query_result = connection.execute(query)
        rows = query_result.fetchall()
        print(rows)
    serialize_rows = []
    for row in rows:
        serialized_row = dict(row)
        serialize_rows.append(serialized_row)
    json_data = json.dumps(serialize_rows)  
    print(json_data)
    return "Hello World!"

@app.route('/gallery')
def gallery():
    query = db.select([emp]).order_by(db.asc(emp.columns.pokemon))

    with engine.connect() as connection:
        query_result = connection.execute(query)
        rows = query_result.fetchall()

    pokemon_data = []
    for row in rows:
        pokemon = {
            'name': row['pokemon'],
            'url': row['url']
        }
        pokemon_data.append(pokemon)
    
    return render_template('gallery.html', pokemon_data=pokemon_data)


if __name__ == '__main__':            
    app.run(debug=True, host="0.0.0.0")