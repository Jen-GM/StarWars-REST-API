from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(50), unique=False, nullable=True)
    hair_color = db.Column(db.String(50), unique=False, nullable=True)
    eye_color = db.Column(db.String(80), unique=False, nullable=True)

    def __repr__(self):
        return '<Character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
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
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "population": self.gender,
            "terrain": self.hair_color,
        }

class Character_favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, ForeignKey('characters.id'), unique=True, nullable=False)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), unique=True, nullable=False)
    character = relationship(Character)
    user = relationship(User)

    def __repr__(self):
        return '<Character_favorite %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "character_id": self.character_id
        }

class Planet_favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_id = db.Column(db.Integer, ForeignKey('planet.id'), unique=True, nullable=False)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), unique=True, nullable=False)
    planet = relationship(Planet)
    user = relationship(User)

    def __repr__(self):
        return '<Planet_favorite %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "character_id": self.character_id
        }