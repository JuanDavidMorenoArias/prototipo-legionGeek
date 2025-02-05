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

    def propose_activity(self, activity, users):
        for user in users:
            if user.role == 'participante':
                user.add_activity_to_inbox(activity)