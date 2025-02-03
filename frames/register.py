import tkinter as tk
from tkinter import ttk, messagebox
import re
import utils

class RegisterFrame(tk.Frame):
    # En esta clase
    def __init__(self, parent, login_frame):
        super().__init__(parent, width=350, height=550, background='white')
        # Yo el propio frame
        self.me = self
        # Parent: la ventana padre
        self.parent = parent
        # el frame login
        self.login_frame = login_frame
        # activa la creacion de widgets
        self.create_widgets()
              
    # Creacion de los widgets del frame, botones, entries y labels de texto
    def create_widgets(self):
        # Texto "Registrarse"
        self.heading = ttk.Label(self, text='Registrarse', foreground='#5b4275', background='white', font=('Trebuchet MS', 23, 'bold'))
        self.heading.place(relx=0.5, rely=0.10, anchor='center')

        # El entry (espacio para insertar el numero de documento)
        self.userID = tk.Entry(self, width=30, foreground='gray', background='white', insertbackground='#5b4275', border=0, font=('Trebuchet MS', 12, 'bold'))
        self.userID.place(relx=0.1, rely=0.20)
        self.userID.insert(0, 'Numero de documento')
        self.write_line_userID = tk.Frame(self, width=300, height=2, background='black').place(relx=0.1, rely=0.25)

        # El entry (espacio para insertar el nombre)
        self.full_name = tk.Entry(self, width=30, foreground='gray', background='white', insertbackground='#5b4275',  border=0, font=('Trebuchet MS', 12, 'bold'))
        self.full_name.place(relx=0.1, rely=0.30)
        self.full_name.insert(0, 'Nombre Completo')
        self.write_line_full_name = tk.Frame(self, width=300, height=2, background='black').place(relx=0.1, rely=0.35)

        # El entry (espacio para insertar el email)
        self.email = tk.Entry(self, width=30, foreground='gray', background='white', insertbackground='#5b4275', border=0, font=('Trebuchet MS', 12, 'bold'))
        self.email.place(relx=0.1, rely=0.40)
        self.email.insert(0, 'Correo Electrónico')
        self.write_line_email = tk.Frame(self, width=300, height=2, background='black').place(relx=0.1, rely=0.45)

        # El entry (espacio para insertar el numero telefonico)
        self.phone = tk.Entry(self, width=30, foreground='gray', background='white', insertbackground='#5b4275', border=0, font=('Trebuchet MS', 12, 'bold'))
        self.phone.place(relx=0.1, rely=0.50)
        self.phone.insert(0, 'Numero Telefónico')
        self.write_line_phone = tk.Frame(self, width=300, height=2, background='black').place(relx=0.1, rely=0.55)

        # El entry (espacio para insertar el contraseña)
        self.password = tk.Entry(self, width=30, foreground='gray', background='white', insertbackground='#5b4275', border=0, font=('Trebuchet MS', 12, 'bold'))
        self.password.place(relx=0.1, rely=0.60)
        self.password.insert(0, 'Contraseña')
        self.write_line_password = tk.Frame(self, width=300, height=2, background='black').place(relx=0.1, rely=0.65)

        # El entry (espacio para confirmar la contraseña antes escrita)
        self.confirm_password = tk.Entry(self, width=30, foreground='gray', background='white', insertbackground='#5b4275', border=0, font=('Trebuchet MS', 12, 'bold'))
        self.confirm_password.place(relx=0.1, rely=0.70)
        self.confirm_password.insert(0, 'Confirmar Contraseña')
        self.write_line_confirm = tk.Frame(self, width=300, height=2, background='black').place(relx=0.1, rely=0.75)

        # Boton para confirmar que nos registramos con ese Numero de documento y contraseña
        self.sign_up_button = tk.Button(self, cursor='hand2', width=42, pady=7, border=0, text='Completar registro', background='#5b4275', foreground='white')
        self.sign_up_button.place(relx=0.1, rely=0.79)
        self.sign_up_button.config(command=self.signup)

        # Texto que guia al usuario al Inicio de sesion si ya tiene una cuenta creada
        self.login_getaway = ttk.Label(self, text=r"¿Ya tienes una cuenta?", background='white', foreground='black', font=('Trebuchet MS', 9, 'bold'))
        self.login_getaway.place(relx=0.20, rely=0.90)

        # Boton cuyo comando nos lleva al logeo, eliminando este frame y agregando el del logeo
        self.sign_in_button = tk.Button(self, width=10, text='Iniciar Sesión', background='white', border=0, cursor='hand2', foreground='#1297cc')
        self.sign_in_button.place(relx=0.60, rely=0.90)
        self.sign_in_button.config(command=self.switch_to_login)
    
    # Funcion que cambia al frame de inicio de sesion
    def switch_to_login(self):
        # Destruir la ventana de registro
        self.destroy()
        # Crear y mostrar la ventana de inicio de sesión
        self.login_frame.reshow()

    # Conecta mediante el metodo bind() las funciones que cree con los eventos FocusIn and Out
    def connect_focus_events(self):
        # Documento de identidad
        self.userID.bind('<FocusIn>', lambda event: utils.userID_on_enter(self.userID))
        self.userID.bind('<FocusOut>', lambda event: utils.userID_on_leave(self.userID))
        # Nombre
        self.full_name.bind('<FocusIn>', lambda event: utils.name_on_enter(self.full_name))
        self.full_name.bind('<FocusOut>', lambda event: utils.name_on_leave(self.full_name))
        # Correo
        self.email.bind('<FocusIn>', lambda event: utils.email_on_enter(self.email))
        self.email.bind('<FocusOut>', lambda event: utils.email_on_leave(self.email))
        # Numero telefonico
        self.phone.bind('<FocusIn>', lambda event: utils.phone_on_enter(self.phone))
        self.phone.bind('<FocusOut>', lambda event: utils.phone_on_leave(self.phone))
        # contraseña
        self.password.bind('<FocusIn>', lambda event: utils.password_on_enter(self.password))
        self.password.bind('<FocusOut>', lambda event: utils.password_on_leave(self.password))
        # confirmar contraseña
        self.confirm_password.bind('<FocusIn>', lambda event: utils.confirm_on_enter(self.confirm_password))
        self.confirm_password.bind('<FocusOut>', lambda event: utils.confirm_on_leave(self.confirm_password))
    
    # Funcion para el boton de Create Account
    def signup(self):
        existing_users = utils.load_existing_users()
        
        # Recolecta los datos para comparar
        username = self.userID.get().strip()
        password = self.password.get().strip()
        confirm = self.confirm_password.get().strip()

        # Verificar que ningun campo quede vacio
        if not (username and password and confirm):
            messagebox.showerror('Error', 'Please fill in all fields')
            return
        
        # Verificar si la contraseña y el confirm coinciden
        if password != confirm:
            messagebox.showerror('Error', 'Passwords do not match')
            return
        
        #Verificar que el nombre de usuario no este ya en uso
        if username in existing_users:
            messagebox.showerror('Error', 'Username already in use')
            return
        
        # Verificar el patrón del Usuario y contraseña usando una expresión regular
        username_requirement = re.match(r"^\S+$", username)
        password_requirement = re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[\w\d!@#$%^&*()-_+=]{8,}$", password)

        if not (username_requirement and password_requirement):
            messagebox.showerror('Error',
                                 '- Username must contain no whitespaces\n'
                                 '- Password must be at least 8 characters longand contain at\n'
                                 '  Least 1 digit, 1 uppercase letter and 1 lowercase letter.\n'
                                 '  No whitespaces allowed')
            return
        
        # Si el registro cumplio con todo, guarda al usuario y contraseña
        # Actualiza la lista de usuarios existentes
        existing_users[username] = password

        with open('users.txt', 'a') as file:
            file.write(f"{username},{password}\n")

        # Mostra el mensaje de exito
        messagebox.showinfo('Success', 'Account created succesfully')
        self.switch_to_login()
