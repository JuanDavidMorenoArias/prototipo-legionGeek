import json
import os

class User:
  def __init__(self,
               full_name,
               password,
               userID=0,
               phone=0,
               email=None,
               role='participant'):
    
    self.full_name=full_name
    self.userID=userID
    self.phone=phone
    self.email=email
    self.password=password
    self.role = role

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
  
