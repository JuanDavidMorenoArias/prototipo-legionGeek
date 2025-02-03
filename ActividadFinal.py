from Actividad import Actividad
class ActividadFinal(Actividad):
    def __init__(self,idea=None,fecha=None,capacidad=0,objetivo=None,duración=0,MR=[]):
        super().__init__(idea,fecha,capacidad,objetivo,duración,MR)
        self.participantes=[]