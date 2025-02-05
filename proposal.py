from activity import Activity
class Proposal(Activity):
    def __init__(self,idea=None,date=None,capacity=0,objective=None,duration=0,MR=[]):
        super().__init__(idea,date,capacity,objective,duration,MR)
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
            'Material Requerido': self.MR
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