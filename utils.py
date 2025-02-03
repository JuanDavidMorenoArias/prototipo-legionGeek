import os

# El estilo de la ventana
def legionGeek_window_style(window):
    window.geometry('1000x600') # tamaño de ventana
    window.resizable(0,0) # no se le podra cambiar el tamaño
    window.title('LegionGeek Actividades') # titulo de la ventana
    window.config(background='white') 
    # Imagen en la barra de titulo  

def load_existing_users():
    try:  # Leer los nombres de usuario existentes desde el archivo users.txt
        with open('users.txt', 'r') as file:
            existing_users = {}
            lines = file.readlines()
            if not lines:  # Verificar si el archivo está vacío
                print("El archivo usuarios se encuentra vacío.")
                return existing_users
            
            for line in lines:
                username, password = line.strip().split(',')
                existing_users[username] = password
            
            return existing_users
        
    except FileNotFoundError:  # Si no existe el archivo, más adelante lo creará
        return {}

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
    if userID == 'Numero de documento':
        entry.config(foreground='black')
    else:
        entry.insert(0, userID.strip())
# Función para manejar el evento de desenfoque del usuario
def userID_on_leave(entry):
    userID = entry.get()
    if userID == '':
        entry.config(foreground='gray')
        entry.insert(0, 'Numero de documento')

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