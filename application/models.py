from .database import db

class Admins(db.Model):
    __tablename__ = "admins"
    user_name = db.Column(db.String, primary_key = True, unique = True)
    password = db.Column(db.String)

class Users(db.Model):
    __tablename__ = "users"
    username = db.Column(db.String, primary_key = True, unique = True)
    password = db.Column(db.String)

class Location(db.Model):
    __tablename__ = "location"
    venue = db.Column(db.String, primary_key = True)
    show_name = db.Column(db.String, db.ForeignKey("shows.show_name"), primary_key = True, nullable = False)
    time = db.Column(db.String)
    capacity = db.Column(db.Integer)
    Theatre = db.Column(db.String)
    city = db.Column(db.String)

class Seats(db.Model):
    __tablename__ = "seats"
    venue = db.Column(db.String, db.ForeignKey("location.venue"), primary_key = True, nullable = False)
    show_name = db.Column(db.String, db.ForeignKey("shows.show_name"), primary_key = True, nullable = False)
    available_seats = db.Column(db.Integer)
    price = db.Column(db.Integer)

class UserSeats(db.Model):
    __tablename__ = "user_seats"
    username = db.Column(db.String, db.ForeignKey("users.username"), primary_key = True, nullable = False)
    user_seats = db.Column(db.Integer)

class Shows(db.Model):
    __tablename__ = "shows"
    show_name = db.Column(db.String, primary_key = True)
    rating = db.Column(db.Integer)
    tags = db.Column(db.String, nullable = False)