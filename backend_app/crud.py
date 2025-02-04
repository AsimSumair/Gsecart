from sqlalchemy.orm import Session
from . import models, schemas

def get_contact_by_phone(db: Session, phone: int):
    return db.query(models.Contact).filter(models.Contact.phone == phone).all()

def get_contact_by_email(db: Session, email: str):
    return db.query(models.Contact).filter(models.Contact.email == email).all()

def create_contact(db: Session, contact: schemas.ContactRequest):
    new_contact = models.Contact(email=contact.email, phone=contact.phone)
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact
