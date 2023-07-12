from flask import Flask, render_template
import sqlalchemy as db
import pandas as pd

app = Flask(__name__)

#engine = db.create_engine('sqlite:///data_base_name.db')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/prevAW')
def prevAW():
    '''
    with engine.connect() as connection:
        query_result = connection.execute(db.text("SELECT pokemon, urls FROM table_name;")).fetchall()
        return render_template('prevAW.html', results=query_result)'''
    engine = db.create_engine('sqlite:///data_base_name.db')
    connection = engine.connect()

    query_result = connection.execute(db.text("SELECT pokemon, urls FROM table_name;")).fetchall()

    df = pd.DataFrame(query_result, columns=['pokemon', 'urls'])

    return render_template('prevAW.html', data=df.to_dict(orient='records'))
    #return render_template('/prevAW.html')

if __name__ == '__main__':            
    app.run(debug=True, host="0.0.0.0")