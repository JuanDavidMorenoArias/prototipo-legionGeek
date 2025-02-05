from datetime import datetime

class DateTime:
    def __init__(self):
        self.timestamp = datetime.now()

    def to_dict(self):
        return {
            "timestamp": self.timestamp.isoformat()
        }

    @staticmethod
    def from_dict(data):
        dt = DateTime()
        dt.timestamp = datetime.fromisoformat(data["timestamp"])
        return dt

    def __str__(self):
        return self.timestamp.strftime("%Y-%m-%d %H:%M:%S")