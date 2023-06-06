from db import get_db

class User:
    def __init__(self, user_id, name, email):
        self.id = user_id
        self.name = name
        self.email = email

    @classmethod
    def create(cls, data):
        db = get_db()
        new_user = db.users.insert_one(data)
        return cls(str(new_user.inserted_id), **data)

    @classmethod
    def get(cls, user_id):
        db = get_db()
        user_data = db.users.find_one({"_id": ObjectId(user_id)})
        if not user_data:
            return None
        return cls(str(user_data['_id']), **user_data)

    @classmethod
    def get_all(cls):
        db = get_db()
        users = []
        for user_data in db.users.find():
            users.append(cls(str(user_data['_id']), **user_data).json())
        return users

    def update(self, data):
        db = get_db()
        db.users.update_one({"_id": ObjectId(self.id)}, {"$set": data})
        self.__dict__.update(data)

    def delete(self):
        db = get_db()
        db.users.delete_one({"_id": ObjectId(self.id)})

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }