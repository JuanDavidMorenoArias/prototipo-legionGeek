from Usuario import Usuario
class Staff(Usuario):
    def __init__(self,nombre=None,id=0,tel=0,email=None,pswd=None):
        super().__init__(nombre,id,tel,email,pswd)
        actividades=[]