from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    birthday = db.Column(db.Date)
    animals = db.relationship('Animal', backref='zookeeper', lazy='dynamic')

class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String(100))  # Corrected 'enviroment' to 'environment'
    open_to_visitors = db.Column(db.Boolean)
    animals = db.relationship('Animal', backref='enclosure', lazy='dynamic')

class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))  # Corrected 'string' to 'String'
    species = db.Column(db.String(100))  # Corrected 'column' to 'Column'
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))  # Corrected 'integer' to 'Integer'
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))  # Corrected 'integer' to 'Integer'
