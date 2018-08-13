# Database related imports
# Make sure to import your tables!
from model import Base, User, Post

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Your database functions are located under here (querying, adding items, etc.)

# Example of adding a student:
def add_student(username1, password1, email1, name1, lastName1, location1):
    print("Added a student!")
    user = User(username=username1, password=password1, email=email1, name=name1, lastName=lastName1, location=location1)
    session.add(user)
    session.commit()

def add_post(cat,text):
	post = Post(category=cat,description=text)
	session.add(post)
	session.commit()

def get_all_students():
    students = session.query(Student).all()
    return students

def check_account(user,password):
    if session.query(User).filter_by(username=user).first() != None and session.query(User).filter_by(username=user).first().password == password:
        return("THIS account exists!")
    else:
        return("This account does not exists!")

def if_account_exist(email1):
	if session.query(User).filter_by(email=email1).first() is not None:
		return True
	return False
def query_by_job():
    posts = session.query(
       Post).filter_by(
       category="jobs").all()
    return posts