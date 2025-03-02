from activity import Activity
class ActivityIns(Activity):
    def __init__(self,idea, date, capacity, objective, duration, required_materials):
        super().__init__(idea,date,capacity,objective,duration,required_materials)
        self.inscritos = []

    def to_dict(self):
        return {
            "idea": self.idea,
            "Fecha": self.date,
            "Capacidad": self.capacity,
            "Objetivos": self.objective,
            "Duracion": self.duration,
            "Material Requerido": self.required_materials,
            "Inscritos": self.inscritos,
            "Actividad": {
                "Inscripciones": 0
            }
        }

    @staticmethod
    def from_dict(data):
        return ActivityIns(
            data["idea"],
            data["Fecha"],
            data["Capacidad"],
            data["Objetivos"],
            data["Duracion"],
            data["Material Requerido"]
        )