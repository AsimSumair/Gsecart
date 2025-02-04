from sqlalchemy import Column, Integer, String
from .database import Base

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True, nullable=False)  
    phone = Column(Integer, index=True, nullable=False)  
