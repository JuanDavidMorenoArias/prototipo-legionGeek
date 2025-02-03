import tkinter as tk
from tkinter import ttk, messagebox
import utils
import frames.register as register

class LogInFrame(tk.Frame):
    def __init__(self, parent, login_callback):
        super().__init__(parent, width=350, height=350, background='white')
        # el mismo frame
        self.me = self
        # para cerrar
        self.login_callback = login_callback
        # la ventana padre 
        self.parent = parent
        # activa la creacion de widgets
        self.create_widgets()

    # Creacion de los widgets como botones, entries y textos para la interfaz de inicio de sesion.
    def create_widgets(self): 
        # Texto "Iniciar Sesión"
        self.heading = ttk.Label(self, text='Iniciar Sesión', foreground='#1297cc', background='#ffffff', font=('Trebuchet MS', 23, 'bold'))
        self.heading.place(relx=0.5, rely=0.1, anchor='center')
        # El entry (espacio para insertar el ID de usuario)
        self.user = tk.Entry(self, width=30, foreground='gray', border=0,background='white', insertbackground='#1297cc', font=('Trebuchet MS', 12, 'bold'))
        self.user.place(relx=0.1, rely=0.3)
        self.user.insert(0, 'ID de usuario')
        # Línea bajo el entry del ID de usuario
        self.write_line_user = tk.Frame(self,width=300,height=2,background='black').place(relx=0.1,rely=0.37)

        # El entry (espacio para insertar la contraseña)
        self.code = tk.Entry(self, width=30, foreground='gray', border=0,background='white',insertbackground='#1297cc', font=('Trebuchet MS', 12, 'bold'))
        self.code.place(relx=0.1, rely=0.5)
        self.code.insert(0, 'Contraseña')
        # Línea bajo el entry de la contraseña
        self.write_line_code = tk.Frame(self,width=300,height=2,background='black').place(relx=0.1,rely=0.57)

        # Boton para confirmar que iniciamos sesion con ese ID de usuario y contraseña
        self.sign_in_button = tk.Button(self, cursor='hand2', width=42, pady=7, border=0, text='Iniciar Sesión',background='#1297cc', foreground='white')
        self.sign_in_button.place(relx=0.1, rely=0.7)
        self.sign_in_button.config(command=self.sign_in)

        # Texto que guia al usuario al registro si no tiene cuenta creada aun
        self.register_getaway = ttk.Label(self, text=r"¿No te has registrado?",background='white', foreground='black', font=('Trebuchet MS', 9, 'bold'))
        self.register_getaway.place(relx=0.20, rely=0.87)
        # Boton cuyo comando nos lleva al registro, eliminando este frame y agregando el del registro
        self.sign_up_button = tk.Button(self, width=8, text='Registrarse',background='white', border=0, cursor='hand2', foreground='#1297cc')
        self.sign_up_button.place(relx=0.65, rely=0.87)
        self.sign_up_button.config(command=self.switch_to_register)

    # Asociar eventos de enfoque a los campos de entrada
    def connect_focus_events(self):
        # Username
        self.user.bind('<FocusIn>', lambda event: utils.user_on_enter(self.user))
        self.user.bind('<FocusOut>', lambda event: utils.user_on_leave(self.user))
        # Password
        self.code.bind('<FocusIn>', lambda event: utils.code_on_enter(self.code))
        self.code.bind('<FocusOut>', lambda event: utils.code_on_leave(self.code))

    # Cambiar al frame de registro
    def switch_to_register(self): 
        # Destruir la ventana de inicio de sesión
        self.place_forget()
        # Crear y mostrar la ventana de registro
        self.register_frame = register.RegisterFrame(self.parent, self.me)
        self.register_frame.place(relx=0.75,rely=0.5, anchor='center')
        self.register_frame.connect_focus_events()

    # Método que verifica el inicio de sesión
    def sign_in(self):
        # Lista de usuarios creados hasta el momento
        existing_users = utils.load_existing_users()
        username = self.user.get().strip()
        password = self.code.get().strip()
        
        # Comprobar si el usuario existe
        if username not in existing_users: 
            messagebox.showerror('Error','¡El usuario no existe!')
    
        # Comprobar si la contraseña es correcta
        else: 
            if existing_users[username] != password:
                messagebox.showerror('Error', '¡Contraseña incorrecta!')
            
            else:
                # Limpiar los campos de entrada
                self.user.delete(0, 'end')
                self.code.delete(0, 'end')
                # Mostrar mensaje de inicio de sesión exitoso
                messagebox.showinfo('Bienvenido','Ha iniciado sesión exitosamente!')
                # Llamar al callback de inicio de sesión
                self.login_callback(True)

    # Mostrar nuevamente el frame de inicio de sesión
    def reshow(self):
        self.place(relx=0.75,rely=0.5, anchor='center')


    