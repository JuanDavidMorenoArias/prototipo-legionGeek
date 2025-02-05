from user import User
class Moderator(User):
    def __init__(self,
               full_name,
               userID,
               password,
               phone,
               email):
        
        super().__init__( full_name, userID, password, phone, email, role='moderador')
        ideas=[]
        proposals=[]
        activities=[]
        participants=[]
        
    def importarideas():
        try:
            with open("ideas.txt", "r") as f:
                return [line.strip() for line in f.readlines()]  # Leer y limpiar espacios
        except FileNotFoundError:
            return []
        
    def propose_activity(self, activity, users):
        for user in users:
            if user.role == 'participante':
                user.add_activity_to_inbox(activity)