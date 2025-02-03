from Actividad import Actividad
class Propuesta(Actividad):
    def __init__(self,idea=None,fecha=None,capacidad=0,objetivo=None,duración=0,MR=[]):
        super().__init__(idea,fecha,capacidad,objetivo,duración,MR)
        self.aprobados=0
        self.desaprobados=0
        self.retroalimentacion=[]