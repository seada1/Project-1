class Event:

    def __init__(self, event_id=0, event_type="", percentage=0):
        self.event_id = event_id,
        self.event_type = event_type,
        self.percentage = percentage


    def __repr__(self):
        return str({
            "event_id": self.event_id,
            "event_type": self.event_type,
            "percentage": self.percentage

        })

    def json(self):
        return {
            "event_id": self.event_id,
            "event_type": self.event_type,
            "percentage": self.percentage
        }