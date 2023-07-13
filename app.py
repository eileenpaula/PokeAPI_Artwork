from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import json

import sqlalchemy as db

import os
import openai
import requests

app = Flask(__name__)

openai.api_key = ""

# Creating Database and Table
engine = db.create_engine('sqlite:///data_base_name.sqlite') #Create data_base_name.sqlite automatically
connection = engine.connect()
metadata = db.MetaData()

# Json.dumps(arr), blob
emp = db.Table('emp', metadata,
              db.Column('pokemon', db.String()),
              db.Column('url', db.String(), nullable=False)
              )

metadata.create_all(engine) #Creates the table

print("table created")

@app.route('/', methods=['GET', 'POST'])
def index(): 
    m = ""
    user_input_class = "contact-container"
    img_class = "ia-container is-hidden"
    reset_class = "reset has-text-centered is-hidden"
    img_url=""
    if request.method == 'POST':
        poke_search = request.form.get('poke-input')
        poke_search = poke_search.lower() # ensures that user input in lowercase
        if not poke_search: #this is where validation
            m = "Please enter a Pokemon name." #if the user doesn't type anything, this will tell them to do so.
        #elif any(char.isdigit(_) for char in poke_search):
        elif not poke_search.isalpha():
            m = "Input should not contain numbers. Please enter a Pokemon name." #if they type numbers, it will ask them to enter a name instead        
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
                image_url = response['data'][0]['url']
                print(image_url)

                user_input_class += " is-hidden"
                img_class = "ia-container"
                reset_class = "reset has-text-centered"
                img_url = image_url

                with engine.connect() as connection:
                    data = {"pokemon":poke_search, "url":image_url}
                    connection.execute(emp.insert(), data)

    print(request.form)
    return render_template('index.html', message = m, user_input_class = user_input_class, img_class = img_class, reset_class = reset_class, img_url = img_url)
    #class names not working

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

@app.route('/prevAW')
def prevAW():
    with engine.connect() as connection:
        query = db.select(emp)
        query_result = connection.execute(query)
        rows = query_result.fetchall()

    pokemon_data = []
    for row in rows:
        pokemon = {
            'name': row['pokemon'],
            'url': row['url']
        }
        pokemon_data.append(pokemon)
    
    return render_template('prevAW.html', pokemon_data=pokemon_data)

if __name__ == '__main__':            
    app.run(debug=True, host="0.0.0.0")