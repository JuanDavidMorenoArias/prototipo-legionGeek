from user import User
class Moderator(User):
    def __init__(self,name=None,id=0,phone=0,email=None,password=None):
        super().__init__(name,id,phone,email,password)
        ideas=[]
        proposals=[]
        activities=[]
        participants=[]