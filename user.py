class User:
  def __init__(self,name=None,id=0,phone=0,email=None,password=None):
    self.name=name
    self.id=id
    self.phone=phone
    self.email=email
    self.password=password

  def set_nombre(self,name):
    self.name=name
  def get_nombre(self):
    return self.name
  
  def set_id(self,id):
    self.id=id
  def get_id(self):
    return self.id
  
  def set_tel(self,phone):
    self.phone=phone
  def get_tel(self):
    return self.phone
  
  def set_email(self,email):
    self.email=email
  def get_email(self):
    return self.email
  
  def __str__(self):
    text=f"{self.name} {self.id} {self.phone} {self.email}"
    return text