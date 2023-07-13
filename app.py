from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

import sqlalchemy as db

app = Flask(__name__)

# Creating Database and Table
engine = db.create_engine('sqlite:///data_base_name.sqlite') #Create data_base_name.sqlite automatically
connection = engine.connect()
metadata = db.MetaData()

# Json.dumps(arr)
emp = db.Table('emp', metadata,
              db.Column('pokemon', db.String()),
              db.Column('url', db.String(), nullable=False)
              )

metadata.create_all(engine) #Creates the table

print("table created")

@app.route('/', methods=['GET', 'POST'])
def index():    
    print(request.form)
    if request.method == 'POST':
        poke_search = request.form.get('poke-input')
        with engine.connect() as connection:
            data = {"pokemon":"this works", "url":"N/A"}
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
    return "Hello World!"

'''
@app.route('/prevAW')
def prevAW():
    engine = db.create_engine('sqlite:///data_base_name.db')
    connection = engine.connect()
    query_result = connection.execute(db.text("SELECT pokemon, urls FROM table_name;")).fetchall()
    df = pd.DataFrame(query_result, columns=['pokemon', 'urls'])
    return render_template('prevAW.html', data=df.to_dict(orient='records'))'''

if __name__ == '__main__':            
    app.run(debug=True, host="0.0.0.0")