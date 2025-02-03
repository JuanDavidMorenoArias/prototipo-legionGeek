from user import User
class Participant(User):
    def __init__(self,name=None,id=0,phone=0,email=None,password=None):
        super().__init__(name,id,phone,email,password)
        activities=[]
        proposals=[]