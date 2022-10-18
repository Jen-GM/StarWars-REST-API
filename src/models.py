from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    character_favorite = db.relationship('Character_favorite', backref='favorite_character', lazy='dynamic',
                                         primaryjoin="User.id == Character_favorite.user_id")
    planet_favorite = db.relationship('Planet_favorite', backref='favorite_character', lazy='dynamic',
                                      primaryjoin="User.id == Planet_favorite.user_id")

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email
        }


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(50), unique=False, nullable=True)
    hair_color = db.Column(db.String(50), unique=False, nullable=True)
    eye_color = db.Column(db.String(80), unique=False, nullable=True)

    def __repr__(self):
        return '<Character %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color
        }


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    population = db.Column(db.String(50), unique=False, nullable=True)
    terrain = db.Column(db.String(50), unique=False, nullable=True)

    def __repr__(self):
        return '<Planet %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "terrain": self.terrain
        }


class Character_favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey(
        'user.id'))
    character_id = db.Column(db.Integer, ForeignKey(
        'character.id'))
    user = db.relationship('User')
    characters = db.relationship('Character')

    def __repr__(self):
        return '<Character_favorite %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id
        }


class Planet_favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey(
        'user.id'))
    planet_id = db.Column(db.Integer, ForeignKey(
        'planet.id'))
    user = db.relationship('User')
    planet = db.relationship('Planet')

    def __repr__(self):
        return '<Planet_favorite %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
        }
