from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base 

# Create the SQLite database engine
engine = create_engine('sqlite:///electronics_components_shop.db', echo=True)

# Function to create tables
def create_tables():
    Base.metadata.create_all(engine)

# Set up the session
Session = sessionmaker(bind=engine)
session = Session()


create_tables()
