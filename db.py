from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///example.db')
db = sessionmaker(bind=engine)()