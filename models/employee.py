class Employee:

    def __init__(self, empl_id="", fname="", lname="",gender="", email="", phone="", position="", address="", user_id="", password=""):
        self.empl_id = empl_id
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.email = email
        self.phone = phone
        self.position = position
        self.address = address
        self.user_id = user_id
        self.password = password

    def __repr__(self):
        return str({
            "empl_id": self.empl_id,
            "fname": self.fname,
            "lname": self.lname,
            "gender": self.gender,
            "email": self.email,
            "phone": self.phone,
            "position": self.position,
            "address": self.address,
            "user_id": self.user_id,
            "password": self.password

        })

    def json(self):
        return {
            "emplId": self.empl_id,
            "fname": self.fname,
            "lname": self.lname,
            "gender": self.gender,
            "email": self.email,
            "phone": self.phone,
            "position": self.position,
            "address": self.address,
            "userId": self.user_id,
            "password": self.password
        }