from datetime import datetime
from date import DateTime

class Idea:
    def __init__(self, description, sender, timestamp=None):
        self.description = description
        self.sender = sender
        self.timestamp = timestamp if timestamp else datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def to_dict(self):
        return {
            'descripcion': self.description,
            'Enviado por': self.sender,
            'Fecha y hora de envio': self.timestamp
        }
    
    @staticmethod
    def from_dict(data):
        return Idea(
            data['descripcion'],
            data['Enviado por'],
            data['Fecha y hora de envio']
        )