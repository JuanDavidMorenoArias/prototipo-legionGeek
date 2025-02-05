import tkinter as tk
from tkinter import ttk, messagebox
import utils
import frames.register as register
from user import User

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
        # El entry (espacio para insertar el numero de documento)
        self.userID = tk.Entry(self, width=30, foreground='gray', border=0,background='white', insertbackground='#1297cc', font=('Trebuchet MS', 12, 'bold'))
        self.userID.place(relx=0.1, rely=0.3)
        self.userID.insert(0, 'Numero de Documento')
        # Línea bajo el entry del numero de documento
        self.write_line_userID = tk.Frame(self,width=300,height=2,background='black').place(relx=0.1,rely=0.37)

        # El entry (espacio para insertar la contraseña)
        self.password = tk.Entry(self, width=30, foreground='gray', border=0,background='white',insertbackground='#1297cc', font=('Trebuchet MS', 12, 'bold'))
        self.password.place(relx=0.1, rely=0.5)
        self.password.insert(0, 'Contraseña')
        # Línea bajo el entry de la contraseña
        self.write_line_password = tk.Frame(self,width=300,height=2,background='black').place(relx=0.1,rely=0.57)

        # Boton para confirmar que iniciamos sesion con ese ID de numero de documento y contraseña
        self.sign_in_button = tk.Button(self, cursor='hand2', width=42, pady=7, border=0, text='Iniciar Sesión',background='#1297cc', foreground='white')
        self.sign_in_button.place(relx=0.1, rely=0.7)
        self.sign_in_button.config(command=self.sign_in)

        # Texto que guia al numero de documento al registro si no tiene cuenta creada aun
        self.register_getaway = ttk.Label(self, text=r"¿No te has registrado?",background='white', foreground='black', font=('Trebuchet MS', 9, 'bold'))
        self.register_getaway.place(relx=0.20, rely=0.87)
        # Boton cuyo comando nos lleva al registro, eliminando este frame y agregando el del registro
        self.sign_up_button = tk.Button(self, width=8, text='Registrarse',background='white', border=0, cursor='hand2', foreground='#5b4275')
        self.sign_up_button.place(relx=0.65, rely=0.87)
        self.sign_up_button.config(command=self.switch_to_register)

    # Asociar eventos de enfoque a los campos de entrada
    def connect_focus_events(self):
        # Username
        self.userID.bind('<FocusIn>', lambda event: utils.userID_on_enter(self.userID))
        self.userID.bind('<FocusOut>', lambda event: utils.userID_on_leave(self.userID))
        # Password
        self.password.bind('<FocusIn>', lambda event: utils.password_on_enter(self.password))
        self.password.bind('<FocusOut>', lambda event: utils.password_on_leave(self.password))

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
        user_id = self.userID.get().strip()
        password = self.password.get().strip()
        
        # Comprobar si el usuario existe
        user = next((user for user in existing_users if user.userID == user_id), None)
        if not user:
            messagebox.showerror('Error', '¡El usuario no existe!')
            return
    
        # Comprobar si la contraseña es correcta

        if user.password != password:
            messagebox.showerror('Error', '¡Contraseña incorrecta!')
            return 
        
        # Limpiar los campos de entrada y definir con que role se entro
        self.user_role = user.role # guarda el rol de usuario
        self.userID.delete(0, 'end')
        self.password.delete(0, 'end')
        # Mostrar mensaje de inicio de sesión exitoso
        messagebox.showinfo('Bienvenido','Ha iniciado sesión exitosamente!')
        # Llamar al callback de inicio de sesión
        self.login_callback(True, self.user_role, user)

    # Mostrar nuevamente el frame de inicio de sesión
    def reshow(self):
        self.place(relx=0.75,rely=0.5, anchor='center')


    