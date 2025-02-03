from activity import Activity
class Proposal(Activity):
    def __init__(self,idea=None,date=None,capacity=0,objective=None,duration=0,MR=[]):
        super().__init__(idea,date,capacity,objective,duration,MR)
        self.approved=0
        self.disapproved=0
        self.feedback=[]