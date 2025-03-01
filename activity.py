class Activity:
    def __init__(self, idea, date, capacity, objective, duration, required_materials):
        self.idea = idea
        self.date = date
        self.capacity = capacity
        self.objective = objective
        self.duration = duration
        self.required_materials = required_materials

    def getIdea(self):
        return self.idea
