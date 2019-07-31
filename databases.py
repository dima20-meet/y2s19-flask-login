from model import Base, User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(name,secret_word):
    """Add a user to the DB."""
    user = User(username=name)
    #there is a line of code missing here, what else does a user need?
    user.hash_password(secret_word)
    session.add(user)
    session.commit()

def get_user(username):
    """Find the first user in the DB, by their username."""
    return session.query(User).filter_by(username=username).first()

def add_user(fav_food):
    food = User(food=fav_food)
    session.add(food)
    session.commit()    

def fav_food(food):
	session.query(User).filter_by(fav_food = food).first().fav_food = food
