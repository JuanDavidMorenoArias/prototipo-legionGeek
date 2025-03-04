#Librerias para creacion de la app
import tkinter as tk
from tkinter import ttk
# Importo la clase de inicio de sesion, registro y funciones
from frames.login import LogInFrame
from frames.intro import IntroFrame
from frames.toggle_menu import ToggleMenuFrame
from frames.inicio_frame import HomeFrame  # Asegúrate de importar HomeFrame
from frames.admin_toggle_menu import AdminToggleMenuFrame
from frames.admin_inicio_frame import AdminHomeFrame  # Asegúrate de importar HomeFrame
from frames.staff_inicio_frame import StaffHomeFrame # Asegurarse de importar las classes staff
from frames.staff_toggle_menu import StaffToggleMenuFrame

import utils

class App():
    # Init va a correr cada que llamemos la clase como en la linea App()
    def __init__(self):

        self.root = tk.Tk() # crea instancia de la app
        utils.legionGeek_window_style(self.root)
        self.entry_show() # Genera la ventana de la app
        self.root.mainloop() # mandatorio la visualización de la app
        return

    def entry_show(self):

        # FRAME DE TITULO Y LOGO
        self.intro_frame = IntroFrame(self.root)
        self.intro_frame.place(relx=0.27,rely=0.5,anchor='center')

        # FRAME DE INICIO DE SESION 
        self.login_frame = LogInFrame(self.root,self.on_login)
        self.login_frame.place(relx=0.75,rely=0.5, anchor='center')
        self.login_frame.connect_focus_events()

    # Lo que pasa cuando iniciamos como admin o como participante  <<< Login callback
    def on_login(self, login_successful, user_role, user):
        if login_successful:
            self.intro_frame.destroy()
            self.login_frame.destroy()
            if user_role == "moderador":
                self.admin_main_show(user)
            elif user_role == "staff":
                self.staff_main_show(user)
            else:
                self.main_show(user)

    # Lo que mostraria si iniciamos como admin
    def admin_main_show(self, user):
        self.admin_home_frame = AdminHomeFrame(self.root, user)
        self.admin_home_frame.place(relx=0.5, rely=0.556, anchor='center')

        self.admin_toggle_menu = AdminToggleMenuFrame(self.root, self.entry_show,
                                                      self.admin_home_frame, user)
        self.admin_toggle_menu.pack(side=tk.TOP,fill=tk.X)
        self.admin_toggle_menu.pack_propagate(False)
        self.admin_toggle_menu.configure(height=70)

    def staff_main_show(self,user):
        self.staff_home_frame = StaffHomeFrame(self.root, user)
        self.staff_home_frame.place(relx=0.5, rely=0.556, anchor='center')

        self.staff_toggle_menu = StaffToggleMenuFrame(self.root, self.entry_show,
                                                  self.staff_home_frame, user)
        self.staff_toggle_menu.pack(side=tk.TOP, fill=tk.X)
        self.staff_toggle_menu.pack_propagate(False)
        self.staff_toggle_menu.configure(height=70)

    
    
    def main_show(self, user):
        self.home_frame = HomeFrame(self.root, user)
        self.home_frame.place(relx=0.5, rely=0.556, anchor='center')

        self.toggle_menu = ToggleMenuFrame(self.root, self.entry_show, self.home_frame, user)
        # Al iniciar sesion se pondra por defecto el frame de inicio
        # Barra superior que no se quitara
        self.toggle_menu.pack(side=tk.TOP,fill=tk.X)
        self.toggle_menu.pack_propagate(False)
        self.toggle_menu.configure(height=70)

        
                    
