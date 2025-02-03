import os

# El estilo de la ventana
def legionGeek_window_style(window):
    window.geometry('1000x600') # tamaño de ventana
    window.resizable(0,0) # no se le podra cambiar el tamaño
    window.title('LegionGeek Actividades') # titulo de la ventana
    window.config(background='white') 
    # Imagen en la barra de titulo  

def load_existing_users():
        
        try: # Leer los nombres de usuario existentes desde el archivo users.txt

            with open('users.txt','r') as file:
                existing_users = {}
                for line in file.readlines():
                    username, password = line.strip().split(',')
                    existing_users[username] = password
            return existing_users
        except FileNotFoundError: # Si no existe el archivo, mas adelante lo creara
            return {}

#####################################################################################################################################

# Estas son funciones que compartian tanto instancias de login y register, entonces las dejo aca para que ambos compartan estas
# en el caso de registro, dicha clase tiene 3 metodos mas debido a que el registro tiene una entrada mas para confirmar la "Password"
# Los siguientes son metodos que agregan calidad, focus in and out para los entries que creé en clases de register y login
# Función para manejar el evento de enfoque del usuario
# tambien se encarga de eliminar espacios en blanco para eliminar sensibilidad 
def user_on_enter(entry):
    name = entry.get()
    entry.delete(0, 'end')
    if name == 'ID de usuario':
        entry.config(foreground='black')
    else:
        entry.insert(0, name.strip())

# Función para manejar el evento de desenfoque del usuario
def user_on_leave(entry):
    name = entry.get()
    if name == '':
        entry.config(foreground='gray')
        entry.insert(0, 'ID de usuario')

# Función para manejar el evento de enfoque de la contraseña
# tambien se encarga de eliminar espacios en blanco para eliminar sensibilidad 
def code_on_enter(entry):
    name = entry.get()
    entry.delete(0, 'end')
    if name == 'Contraseña':
        entry.config(foreground='black')
    else:
        entry.insert(0, name.strip())

# Función para manejar el evento de desenfoque de la contraseña
def code_on_leave(entry):
    name = entry.get()
    if name == '':
        entry.config(foreground='gray')
        entry.insert(0, 'Contraseña')

# cuando enfoco al entry, desaparece el "Confirm Password" en gris, escribo en negro 
# tambien se encarga de eliminar espacios en blanco para eliminar sensibilidad        
def confirm_on_enter(entry):
    name = entry.get()
    entry.delete(0, 'end')
    if name == 'Confirm Password':
        entry.config(foreground='black')
    else: entry.insert(0,name.strip())
    
# cuando desenfoco el entry, aparece el "Confirm Password" en gris (si no hay nada escrito)
def confirm_on_leave(entry):
    name = entry.get()
    if name == '':
        entry.config(foreground='gray')
        entry.insert(0, 'Confirm Password')

#####################################################################################################################################