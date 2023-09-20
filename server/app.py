#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.filter(Animal.id == id).first()
    if not animal:
        response_body ='<h1>404 animal not found</h1>'
        response = make_response(response_body,404)
        return response
    
    response_body = f'''
    <ul>
    <li>Name: {animal.name}</li>
    <li>Species:{animal.species}</li>
    <li>Zookeeper: {animal.zookeeper.name}</li>
    <li>Enclosure: {animal.enclosure.environment}</li>
    </ul>
    '''
    response = make_response(response_body,200)
    return response

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.filter(Zookeeper.id == id).first()

    response_body = f'<h1>Zookeeper ID {zookeeper.id}</h1>'
    response_body += f'<ul><li>Name: {zookeeper.name}</li>'
    response_body += f'<li>Birthday: {zookeeper.birthday}</li>'
    
    animals = [animal.name for animal in zookeeper.animals]

    if not animals:
        response_body += f'<li>Cares for no animals at this time.</li></ul>'
    else:
        response_body += f'<li>Cares for the following animals:</li><ul>'
        for animal in animals:
            response_body += f'<li>{animal}</li>'
        response_body += '</ul></ul>'

    response = make_response(response_body, 200)

    return response


@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.filter(Enclosure.id == id).first()

    response_body = f'<ul><li>Enclosure ID {enclosure.id}</li>' 
    response_body += f'<li>Enviroment:  {enclosure.environment}</li>'
    response_body +=  f'<li>Open to Visitors: {enclosure.open_to_visitors}</li>'

     
    animals = [animal.name for animal in enclosure.animals]

    if not animals:
        response_body += f'<li>No animals in this enclosure at this time.</li></ul>'
    else:
        response_body += f'<li>Contains the following animals:</li><ul>'
        for animal in animals:
            response_body += f'<li>{animal}</li>'
        response_body += '</ul></ul>'

    response = make_response(response_body, 200)

    return response


if __name__ == '__main__':
    app.run(port=5555, debug=True)
