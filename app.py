from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#engine = db.create_engine('sqlite:///data_base_name.db')

@app.route('/', methods=['GET', 'POST'])
#@app.route('/index', methods=['GET', 'POST'])
def index():
    print("THIS METHOD IS ", request.method)
    if request.method == "POST":
        print("THIS IS A POST REQUEST")
        print(request.values)
        poke_search = request.form.get('poke-input')
        print(request.form)
    return render_template('index.html')

@app.route('/prevAW')
def prevAW():
    
    #with engine.connect() as connection:
        #query_result = connection.execute(db.text("SELECT pokemon, urls FROM table_name;")).fetchall()
        #return render_template('prevAW.html', results=query_result)

    engine = db.create_engine('sqlite:///data_base_name.db')
    connection = engine.connect()

    query_result = connection.execute(db.text("SELECT pokemon, urls FROM table_name;")).fetchall()

    df = pd.DataFrame(query_result, columns=['pokemon', 'urls'])

    return render_template('prevAW.html', data=df.to_dict(orient='records'))
    #return render_template('/prevAW.html')
'''
class Images(db.Model):
    pokemon_name = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)'''

if __name__ == '__main__':            
    app.run(debug=True, host="0.0.0.0")