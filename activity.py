class Activity:
    def __init__(self, idea, date, capacity, objective, duration, required_materials):
        self.idea = idea
        self.date = date
        self.capacity = capacity
        self.objective = objective
        self.duration = duration
        self.required_materials = required_materials

    def to_dict(self):
        return {
            "idea": self.idea,
            "date": self.date,
            "capacity": self.capacity,
            "objective": self.objective,
            "duration": self.duration,
            "required_materials": self.required_materials
        }

    @staticmethod
    def from_dict(data):
        return Activity(
            data["idea"],
            data["date"],
            data["capacity"],
            data["objective"],
            data["duration"],
            data["required_materials"]
        )