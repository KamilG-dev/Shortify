from sqlalchemy.orm import session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('postgresql://admin:admin@database:5432/shortify')
SessionLocal = session.sessionmaker(autocommit=False, autoflush=False, bind=engine)