from database.database import Base
from database.models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import session

engine = create_engine('postgresql+psycopg2://admin:admin@localhost:8011/shortify', pool_pre_ping=True)
SessionLocal = session.sessionmaker(autocommit=False, autoflush=False, bind=engine)
_session = SessionLocal()
Base.metadata.create_all(engine)
_session.commit()