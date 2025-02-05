import os
import json
from user import User
from idea import Idea
from proposal import Proposal

# Carga las ideas existentes desde el archivo json con las ideas
def load_ideas(filename='ideas.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                data = json.load(file)
                if not data:
                    return []
                return [Idea.from_dict(idea) for idea in data]
            except json.JSONDecodeError:
                return []
    return []

# Carga las porpuestas existentes desde el archivo json con las propuestas
def load_proposals(filename='proposals.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                data = json.load(file)
                if not data:
                    return []
                return [Proposal.from_dict(proposal) for proposal in data]
            except json.JSONDecodeError:
                return []
    return []

# guarda las ideas en el JSON
def save_idea(new_idea, filename='ideas.json'):
    existing_ideas = load_ideas(filename)
    existing_ideas.append(new_idea)

    with open(filename, 'w') as file:
        json.dump([idea.to_dict() for idea in existing_ideas], file)
        
# guarda las propuestas en el JSON
def save_proposal(new_proposal, filename='proposals.json'):
    existing_proposals = load_proposals(filename)
    existing_proposals.append(new_proposal)

    with open(filename, 'w') as file:
        json.dump([proposal.to_dict() for proposal in existing_proposals], file)        
        
# Carga los usuarios existentes desde el archivo json con los usuarios
def load_existing_users(filename='users.json'): # recibe el nombre del archivo
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                data = json.load(file)
                if not data: # Verificar si el archivo esta vacío
                    return []
                return [User.from_dict(user) for user in data]
            except json.JSONDecodeError: #Manejar el caso de un archivo vacio o malformado
                return []
    return [] # si existe el archivo, retorna

# guardar los usuarios en el JSON
def save_users(users, filename='users.json'):
    with open(filename, 'w') as file:
        json.dump([user.to_dict() for user in users], file)
        
# El estilo de la ventana
def legionGeek_window_style(window):
    window.geometry('1000x600') # tamaño de ventana
    window.resizable(0,0) # no se le podra cambiar el tamaño
    window.title('LegionGeek Actividades') # titulo de la ventana
    window.config(background='white') 
    # Imagen en la barra de titulo  

#####################################################################################################################################

# Estas son funciones que compartian tanto instancias de login y register, entonces las dejo aca para que ambos compartan estas
# en el caso de registro, dicha clase tiene 3 metodos mas debido a que el registro tiene una entrada mas para confirmar la "Password"
# Los siguientes son metodos que agregan calidad, focus in and out para los entries que creé en clases de register y login
# Función para manejar el evento de enfoque del usuario
# tambien se encarga de eliminar espacios en blanco para eliminar sensibilidad 



# NUMERO DE DOCUMENTO
def userID_on_enter(entry):
    userID = entry.get()
    entry.delete(0, 'end')
    if userID == 'Numero de Documento':
        entry.config(foreground='black')
    else:
        entry.insert(0, userID.strip())
# Función para manejar el evento de desenfoque del usuario
def userID_on_leave(entry):
    userID = entry.get()
    if userID == '':
        entry.config(foreground='gray')
        entry.insert(0, 'Numero de Documento')

#NOMBRE
def name_on_enter(entry):
    name = entry.get()
    entry.delete(0, 'end')
    if name == 'Nombre Completo':
        entry.config(foreground='black')
    else:
        entry.insert(0, name.strip())
# Función para manejar el evento de desenfoque del usuario
def name_on_leave(entry):
    name = entry.get()
    if name == '':
        entry.config(foreground='gray')
        entry.insert(0, 'Nombre Completo')

#EMAIL
def email_on_enter(entry):
    email = entry.get()
    entry.delete(0, 'end')
    if email == 'Correo Electrónico':
        entry.config(foreground='black')
    else:
        entry.insert(0, email.strip())
# Función para manejar el evento de desenfoque del usuario
def email_on_leave(entry):
    email = entry.get()
    if email == '':
        entry.config(foreground='gray')
        entry.insert(0, 'Correo Electrónico')


# NUMERO TELEFONICO
def phone_on_enter(entry):
    phone = entry.get()
    entry.delete(0, 'end')
    if phone == 'Numero Telefónico':
        entry.config(foreground='black')
    else:
        entry.insert(0, phone.strip())
# Función para manejar el evento de desenfoque del usuario
def phone_on_leave(entry):
    phone = entry.get()
    if phone == '':
        entry.config(foreground='gray')
        entry.insert(0, 'Numero Telefónico')

#CONTRASEÑA
# Función para manejar el evento de enfoque de la contraseña
# tambien se encarga de eliminar espacios en blanco para eliminar sensibilidad 
def password_on_enter(entry):
    password = entry.get()
    entry.delete(0, 'end')
    if password == 'Contraseña':
        entry.config(foreground='black')
    else:
        entry.insert(0, password.strip())
# Función para manejar el evento de desenfoque de la contraseña
def password_on_leave(entry):
    password = entry.get()
    if password == '':
        entry.config(foreground='gray')
        entry.insert(0, 'Contraseña')

# CONFIRMAR CONTRASEÑA
# cuando enfoco al entry, desaparece el "Confirm Password" en gris, escribo en negro 
# tambien se encarga de eliminar espacios en blanco para eliminar sensibilidad        
def confirm_on_enter(entry):
    password_confirmation = entry.get()
    entry.delete(0, 'end')
    if password_confirmation == 'Confirmar Contraseña':
        entry.config(foreground='black')
    else: entry.insert(0,password_confirmation.strip())  
# cuando desenfoco el entry, aparece el "Confirm Password" en gris (si no hay nada escrito)
def confirm_on_leave(entry):
    password_confirmation = entry.get()
    if password_confirmation == '':
        entry.config(foreground='gray')
        entry.insert(0, 'Confirmar Contraseña')



#####################################################################################################################################