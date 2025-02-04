from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import get_db
from .contact_node import ContactNode  

router = APIRouter()

@router.post("/resolve-contact", response_model=schemas.ContactResponse)
def resolve_contact(contact: schemas.ContactRequest, db: Session = Depends(get_db)):
    if not contact.email or not contact.phone:
        raise HTTPException(status_code=400, detail="Email or phone number is missing.")
    contact_map = {}
    def get_or_create_node(contact):
        if contact.id in contact_map:
            return contact_map[contact.id]
        else:
            new_node = ContactNode(contact.id, contact.email, contact.phone)
            contact_map[contact.id] = new_node
            return new_node
    root = None
    contacts_by_phone = crud.get_contact_by_phone(db, contact.phone)
    if contacts_by_phone:
        for existing_contact in contacts_by_phone:
            new_node = get_or_create_node(existing_contact)
            if not root:
                root = new_node
            else:
                root.link(new_node) 
    contacts_by_email = crud.get_contact_by_email(db, contact.email)
    if contacts_by_email:
        for existing_contact in contacts_by_email:
            new_node = get_or_create_node(existing_contact)
            if not root:
                root = new_node
            else:
                root.link(new_node)  
    if root:
        root.add_email(contact.email)
        root.add_phone(contact.phone)
        new_contact = crud.create_contact(db, contact)
        new_node = get_or_create_node(new_contact)
        root.link(new_node)
    if not contacts_by_phone and not contacts_by_email:
        new_contact = crud.create_contact(db, contact)
        root = get_or_create_node(new_contact)

    response_contact_ids = []
    response_emails = set()
    response_phones = set()
    visited_nodes = set()

    def traverse_tree(node: ContactNode):
        """Recursively traverse the tree to collect contact information in sequence order."""
        if node in visited_nodes:
            return
        visited_nodes.add(node)

        response_contact_ids.append(node.contact_ids[0]) 
        response_emails.update(node.emails)
        response_phones.update(node.phones)

        for edge in node.edges:
            traverse_tree(edge) 

    traverse_tree(root)

    return schemas.ContactResponse(
        contactIds=response_contact_ids,  
        emails=sorted(response_emails),
        phones=sorted(response_phones)
    )
