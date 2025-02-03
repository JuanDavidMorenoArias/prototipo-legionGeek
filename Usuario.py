class Usuario:
  def __init__(self,nombre=None,id=0,tel=0,email=None,pswd=None):
    self.nombre=nombre
    self.id=id
    self.tel=tel
    self.email=email
    self.pswd=pswd
  def set_nombre(self,nombre):
    self.nombre=nombre
  def get_nombre(self):
    return self.nombre
  def set_id(self,id):
    self.id=id
  def get_id(self):
    return self.id
  def set_tel(self,tel):
    self.tel=tel
  def get_tel(self):
    return self.tel
  def set_email(self,email):
    self.email=email
  def get_email(self):
    return self.email
  def __str__(self):
    texto=f"{self.nombre} {self.id} {self.tel} {self.email}"
    return texto