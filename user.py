class User:
  def __init__(self,
               full_name,
               userID,
               password,
               phone=0,
               email=None,
               role='participant'):
    
    self.full_name=full_name
    self.userID=userID
    self.password=password
    self.phone=phone
    self.email=email
    self.role = role

  # recibe un Usuario y lo convierte a un diccionario con sus propiedades
  def to_dict(self):
    return {
      "full_name": self.full_name,
      "userID": self.userID,
      "password": self.password,
      "phone": self.phone,
      "email": self.email,
      "role": self.role,
    }
  
  # recibe un diccionario y lo convierte a un objeto Usuario.
  @staticmethod
  def from_dict(data):
    return User(
      data["full_name"],
      data["userID"],
      data["password"],
      data["phone"],
      data["email"],
      data["role"],
    )


  # setting y gettings, a excepción de la contraseña y el role ya que estos son intransferibles.
  def set_full_name(self,full_name):
    self.full_name=full_name
  def get_full_name(self):
    return self.full_name
  
  def set_userID(self,userID):
    self.userID=userID
  def get_userID(self):
    return self.userID
  
  def set_phone(self,phone):
    self.phone=phone
  def get_phone(self):
    return self.phone
  
  def set_email(self,email):
    self.email=email
  def get_email(self):
    return self.email
  
  def get_role(self):
    return self.role
  
