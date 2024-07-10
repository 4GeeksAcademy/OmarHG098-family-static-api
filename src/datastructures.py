
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []
        
    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.name,
            "age": self.age,
            "lucky_numbers": self.lucky_numbers
        }

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if member.get("id", None) is None:
            member["id"] = self._generateId()
        self._members.append(member)
        return self._members

    def delete_member(self, id):
        for position, member in enumerate(self._members):
            if member["id"] == id:
                self._members.pop(position)
                return True
        return False

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return
        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
