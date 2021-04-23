from flask import Flask,request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= 'sqlite:///test.db'
db=SQLAlchemy(app)

class Party(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80)) # название события
    theme = db.Column(db.String(80)) # название темы вечеринки, тематика
    date_time = db.Column(db.String(80)) # время начала вечеринки
    dress_code = db.Column(db.String(80)) # дресс-код
    comments = db.Column(db.String(80)) # кодекс тусовки или комментарии к ней 
    #rating = db.Column(db.Integer)

@app.route('/add_party', methods=['POST'])
def add_party():
    party_data = request.get_json()

    new_party = Party(title=party_data['title'], theme=party_data['theme'], date_time=party_data['date_time'], dress_code=party_data['dress_code'],comments=party_data['comments'] ) #, rating=party_data['rating'])

    db.session.add(new_party)
    db.session.commit()

    return 'Done', 201

@app.route('/parties')
def parties():
    party_list = Party.query.all()
    parties = []

    for party in party_list:
        parties.append({'title' : party.title , 'theme' : party.theme, 'date_time' : party.date_time, 'dress_code': party.dress_code,'comments': party.comments })#, 'rating' : party.rating})
    
    #print(parties)
    return jsonify({'parties' : parties})

if __name__ =='__main__':
    app.run(debug=True,port=5000)
    #app.run(debug=True,host='192.168.1.10')