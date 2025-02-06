from activity import Activity
class Proposal(Activity):
    def __init__(self,idea, date, capacity, objective, duration, required_materials):
        super().__init__(idea,date,capacity,objective,duration,required_materials)
        self.approved=0
        self.disapproved=0
        self.feedback=[]
        
    def to_dict(self):
        return {
            'idea': self.idea,
            'Fecha': self.date,
            'Capacidad': self.capacity,
            'Objetivos': self.objective,
            'Duracion': self.duration,
            'Material Requerido': self.required_materials,
            'Aprobados': self.approved,
            'Rechazados': self.disapproved,
            'Feedback': self.feedback
        }
        
    @staticmethod
    def from_dict(data):
        return Proposal(
            data['idea'],
            data['Fecha'],
            data['Capacidad'],
            data['Objetivos'],
            data['Duracion'],
            data['Material Requerido']
        )