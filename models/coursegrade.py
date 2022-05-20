class CourseGrade:

    def __init__(self, grade_id="", grading_format="", grade="", grade_status="", event_id=""):
        self.grade_id = grade_id,
        self.grading_format = grading_format,
        self.grade = grade,
        self.grade_status = grade_status,
        self.event_id = event_id


    def __repr__(self):
        return str({
            "grade_id": self.grade_id,
            "grading_format": self.grading_format,
            "grade": self.grade,
            "grade_status": self.grade_status,
            "event_id": self.event_id
        })

    def json(self):
        return {
            "grade_id": self.grade_id,
            "grading_format": self.grading_format,
            "grade": self.grade,
            "grade_status": self.grade_status,
            "event_id": self.event_id
        }