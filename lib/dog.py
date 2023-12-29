from models import Dog
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

def create_table(Base, engine):
   # Create the SQLite database engine
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
     
    engine = create_engine('sqlite:///dogs.db')
    create_table(Base)    

    
def save(session, dog):

    session.add(dog)
    session.commit()

# Create the SQLite database engine
engine = create_engine('sqlite:///dogs.db')

# Bind the engine to a session
Session = sessionmaker(bind=engine)
session = Session()
        
joey = Dog(
        name="joey", 
        breed="cocker spaniel")
save(session, joey)
    

def get_all(session):
    
    dogs = session.query(Dog).all()
    return dogs


def find_by_name(session, name):
    dog = session.query(Dog).filter_by(name = name).first()
    return dog

def find_by_id(session, id):
    dog = session.query(Dog).filter_by(id = id).first()
    return dog

def find_by_name_and_breed(session, name, breed):
    dog = session.query(Dog).filter_by(name=name, breed=breed).first()
    return dog

def update_breed(session, dog, breed):
    dog.breed = session.query(Dog).filter_by(id=dog.id).first()
    dog.breed = breed
    session.commit()    