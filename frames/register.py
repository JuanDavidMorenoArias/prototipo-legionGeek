import tkinter as tk
from tkinter import ttk, messagebox
import re
import utils

class RegisterFrame(tk.Frame):
    # En esta clase
    def __init__(self, parent, login_frame):
        super().__init__(parent, width=350, height=450, background='white')
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
        # Texto "Sign Up"
        self.heading = ttk.Label(self, text='Sign Up', foreground='orange', background='white', font=('Trebuchet MS', 23, 'bold'))
        self.heading.place(relx=0.5, rely=0.14, anchor='center')
        # El entry (espacio para insertar el Username)
        self.user = tk.Entry(self, width=30, foreground='gray', background='white', border=0, font=('Trebuchet MS', 12, 'bold'))
        self.user.place(relx=0.1, rely=0.3)
        self.user.insert(0, 'Username')
        self.write_line_user = tk.Frame(self, width=300, height=2, background='black').place(relx=0.1, rely=0.35)
        # El entry (espacio para insertar el Password)
        self.code = tk.Entry(self, width=30, foreground='gray', background='white', border=0, font=('Trebuchet MS', 12, 'bold'))
        self.code.place(relx=0.1, rely=0.45)
        self.code.insert(0, 'Password')
        self.write_line_code = tk.Frame(self, width=300, height=2, background='black').place(relx=0.1, rely=0.50)
        # El entry (espacio para confirmar la Password antes escrita)
        self.confirm_code = tk.Entry(self, width=30, foreground='gray', background='white', border=0, font=('Trebuchet MS', 12, 'bold'))
        self.confirm_code.place(relx=0.1, rely=0.6)
        self.confirm_code.insert(0, 'Confirm Password')
        self.write_line_confirm = tk.Frame(self, width=300, height=2, background='black').place(relx=0.1, rely=0.65)
        # Boton para confirmar que nos registramos con ese Username y Password
        self.sign_up_button = tk.Button(self, cursor='hand2', width=42, pady=7, border=0, text='Create account', background='orange', foreground='white')
        self.sign_up_button.place(relx=0.1, rely=0.76)
        self.sign_up_button.config(command=self.signup)
        # Texto que guia al usuario al Inicio de sesion si ya tiene una cuenta creada
        self.login_getaway = ttk.Label(self, text=r"I have an account", background='white', foreground='black', font=('Trebuchet MS', 9, 'bold'))
        self.login_getaway.place(relx=0.25, rely=0.91)
        # Boton cuyo comando nos lleva al logeo, eliminando este frame y agregando el del logeo
        self.sign_in_button = tk.Button(self, width=8, text='Sign In', background='white', border=0, cursor='hand2', foreground='orange')
        self.sign_in_button.place(relx=0.59, rely=0.91)
        self.sign_in_button.config(command=self.switch_to_login)
    
    # Funcion que cambia al frame de inicio de sesion
    def switch_to_login(self):
        # Destruir la ventana de registro
        self.destroy()
        # Crear y mostrar la ventana de inicio de sesión
        self.login_frame.reshow()

    # Conecta mediante el metodo bind() las funciones que cree con los eventos FocusIn and Out
    def connect_focus_events(self):
        # Username
        self.user.bind('<FocusIn>', lambda event: utils.user_on_enter(self.user))
        self.user.bind('<FocusOut>', lambda event: utils.user_on_leave(self.user))
        # Password
        self.code.bind('<FocusIn>', lambda event: utils.code_on_enter(self.code))
        self.code.bind('<FocusOut>', lambda event: utils.code_on_leave(self.code))
        # Confirm Password
        self.confirm_code.bind('<FocusIn>', lambda event: utils.confirm_on_enter(self.confirm_code))
        self.confirm_code.bind('<FocusOut>', lambda event: utils.confirm_on_leave(self.confirm_code))
    
    # Funcion para el boton de Create Account
    def signup(self):
        existing_users = utils.load_existing_users()
        
        # Recolecta los datos para comparar
        username = self.user.get().strip()
        password = self.code.get().strip()
        confirm = self.confirm_code.get().strip()

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
