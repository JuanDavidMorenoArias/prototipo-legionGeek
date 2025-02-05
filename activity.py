class Activity:
    def __init__(self,idea=None,date=None,capacity=0,objective=None,duration=0,MR=[]):
        self.idea=idea
        self.date=date
        self.capacity=capacity
        self.objective=objective
        self.duration=duration
        self.MR=MR
    
    def to_dict(self):
        return {
            'idea': self.idea,
            'Fecha': self.date,
            'Capacidad': self.capacity,
            'Objetivos': self.objective,
            'Duracion': self.duration,
            'Material Requerido': self.MR
        }
        
    @staticmethod
    def from_dict(data):
        return Activity(
            data['idea'],
            data['Fecha'],
            data['Capacidad'],
            data['Objetivos'],
            data['Duracion'],
            data['Material Requerido']
        )