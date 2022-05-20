class Form:

    def __init__(self, form_id=0, empl_id=0, location="", description="", cost=0,  attachment="",event_id=0, grade_id=0, status="", award_amount=0):
        self.form_id = form_id,
        self.empl_id = empl_id,
        self.location = location,
        self.description = description,
        self.cost = cost,
        self.attachment = attachment,
        self.event_id = event_id,
        self.grade_id = grade_id,
        self.status = status,
        self.award_amount = award_amount

    def __repr__(self):
        return str({
            "form_id": self.form_id,
            "empl_id": self.empl_id,
            "location": self.location,
            "description": self.description,
            "cost": self.cost,
            "attachment": self.attachment,
            "event_id": self.event_id,
            "grade_id": self.grade_id,
            "status": self.status,
            "award_amount": self.award_amount


        })

    def json(self):
        return {
            "formId": self.form_id,
            "emplId": self.empl_id,
            "location": self.location,
            "description": self.description,
            "cost": self.cost,
            "attachment": self.attachment,
            "eventId": self.event_id,
            "gradeId": self.grade_id,
            "status": self.status,
            "awardAmount": self.award_amount
        }

    # def __eq__(self, other):
    #     if not other:
    #         return False
    #
    #     if not isinstance(other, Form):
    #         return False
    #
    #     # for value1, value2 in zip(vars(self).values(), vars(other).values()):
    #     #     if value1 != value2:
    #     #         return False
    #     #
    #     # return True
    #
    #     return self.__dict__ == other.__dict__

    # def _test():
        # movie1 = Movie()
        # movie2 = Movie()
        #
        # print(movie1 == movie2)
        #
        # movie1 = Movie(title="Thor", price=7)
        # movie2 = Movie(title="Thor", price=7)
        #
        # print(movie1 == movie2)

# if __name__ == '__main__':
#     _test()
#
