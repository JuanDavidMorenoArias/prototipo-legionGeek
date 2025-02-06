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
            "Fecha": self.date,
            "Capacidad": self.capacity,
            "Objetivos": self.objective,
            "Duracion": self.duration,
            "Material Requerido": self.required_materials
        }

    @staticmethod
    def from_dict(data):
        return Activity(
            data["idea"],
            data["Fecha"],
            data["Capacidad"],
            data["Objetivos"],
            data["Duracion"],
            data["Material Requerido"]
        )