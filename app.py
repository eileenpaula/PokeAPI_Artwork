from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import json

import sqlalchemy as db

import os
import openai
import requests

app = Flask(__name__)

openai.api_key = "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"

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
    if request.method == 'POST':
        poke_search = request.form.get('poke-input')

        response = requests.get("https://pokeapi.co/api/v2/pokemon/" + poke_search).json()
        desc = "Generate a fully colored, realistic art piece with a colorful background based on the following:\n\nPokemon: " + poke_search + "\nDescription:\n"
        desc += requests.get(response["species"]["url"]).json()["flavor_text_entries"][0]["flavor_text"]
        response = openai.Image.create(
            prompt=desc,
            n=1,
            size="1024x1024"
            )
        image_url = response['data'][0]['url']

        with engine.connect() as connection:
            data = {"pokemon":poke_search, "url":image_url}
            connection.execute(emp.insert(), data)

    
    print(request.form)
    return render_template('index.html')

@app.route('/testing', methods=['GET', 'POST'])
def testing(): 
    with engine.connect() as connection:
        query = db.select(emp)
        query_result = connection.execute(query)
        rows = query_result.fetchall()
        print(rows)
    # serialize_rows = []
    # for row in rows:
    #     serialized_row = dict(row)
    #     serialize_rows.append(serialized_row)
    # json_data = json.dumps(serialize_rows)  
    # print(json_data)
    return "Hello World!"

@app.route('/prevAW')
def prevAW():
    return render_template('prevAW.html')

if __name__ == '__main__':            
    app.run(debug=True, host="0.0.0.0")