from sqlalchemy import Column, Integer, String
from database.database import Base

class Url(Base):
    __tablename__ = 'url'

    id = Column(Integer, primary_key=True)
    long_url = Column(String(255))
    short_url = Column(String(255))