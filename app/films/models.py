from app.db import db, BaseModelMixin

class Film(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(150))
    length = db.Column(db.Integer)
    year = db.Column(db.Integer)
    director = db.Column(db.String(150))
    actors = db.relationship('Actor', backref='film', lazy = False, cascade = 'all, delete-orphan')

    def __init__(self, title, length, year, director, actors=[]):
        self.title = title
        self.length = length
        self.year = year
        self.director = director
        self.actors = actors

    def __repr__(self):
        return f'Film({self.title})'
    
    def __repr__(self):
        return f'{self.title}'

class Actor(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250))
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'), nullable= False)

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f'Actor({self.name})'
    
    def __str__(self):
        return f'{self.name}'