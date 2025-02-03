import json
import os

class User:
  def __init__(self,full_name,userID=0,phone=0,email=None,password=None):
    self.full_name=full_name
    self.userID=userID
    self.phone=phone
    self.email=email
    self.password=password

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
  
  def __str__(self):
    text=f"{self.name} {self.id} {self.phone} {self.email}"
    return text