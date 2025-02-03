from Usuario import Usuario
class Moderador(Usuario):
    def __init__(self,nombre=None,id=0,tel=0,email=None,pswd=None):
        super().__init__(nombre,id,tel,email,pswd)
        ideas=[]
        propuestas=[]
        actividades=[]
        participantes=[]