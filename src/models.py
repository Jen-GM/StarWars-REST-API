from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    character_favorite = db.relationship('Character_favorite', backref='author', lazy='dynamic',
                                         primaryjoin="User.id == Character_favorite.user_id")
    planet_favorite = db.relationship('Planet_favorite', backref='author', lazy='dynamic',
                                      primaryjoin="User.id == Planet_favorite.user_id")

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(50), unique=False, nullable=True)
    hair_color = db.Column(db.String(50), unique=False, nullable=True)
    eye_color = db.Column(db.String(80), unique=False, nullable=True)
    character_favorite = db.relationship('Character_favorite', lazy=True)

    def __repr__(self):
        return '<Character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "character_favorite": self.character_favorite
        }


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    population = db.Column(db.String(50), unique=False, nullable=True)
    terrain = db.Column(db.String(50), unique=False, nullable=True)
    planet_favorite = db.relationship('Planet_favorite', lazy=True)

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "population": self.gender,
            "terrain": self.hair_color,
            "planet_favorite": self.planet_favorite
        }


class Character_favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey(
        'user.id'), unique=True, nullable=False)
    character_id = db.Column(db.Integer, ForeignKey(
        'character.id'), unique=True, nullable=False)

    def __repr__(self):
        return '<Character_favorite %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id
        }


class Planet_favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey(
        'user.id'), unique=True, nullable=False)
    planet_id = db.Column(db.Integer, ForeignKey(
        'planet.id'), unique=True, nullable=False)

    def __repr__(self):
        return '<Planet_favorite %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
        }
