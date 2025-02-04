
class ContactNode:
    def __init__(self, contact_id, email, phone):
        self.contact_ids = [contact_id]
        self.emails = [email]
        self.phones = [phone]
        self.next = None  
        self.prev = None  
        self.edges = []  

    def link(self, other_node):
        """Link another node as a child in the tree structure."""
        if other_node not in self.edges:
            self.edges.append(other_node)

    def add_email(self, email):
        if email not in self.emails:
            self.emails.append(email)

    def add_phone(self, phone):
        if phone not in self.phones:
            self.phones.append(phone)

    def add_contact_id(self, contact_id):
        if contact_id not in self.contact_ids:
            self.contact_ids.append(contact_id)
