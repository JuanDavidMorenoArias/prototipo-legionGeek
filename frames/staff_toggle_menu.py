import sys
import tkinter as tk
from tkinter import ttk
from frames.staff_biblioteca_frame import StaffLibraryFrame
# aqui se tendran que importar los frames que sean del usuario staff

class StaffToggleMenuFrame(tk.Frame):
    # En esta clase
    def __init__(self,parent, log_out_callback, home_frame, user):
        super().__init__(parent,width=1000, background='#B79C27',
                         highlightbackground='white', highlightthickness=1)    
        self.parent = parent
        self.home_frame = home_frame
        self.user = user
        self.log_out_callback = log_out_callback
        self.bar = StaffSideBarFrame(self.parent,self, self.home_frame, self.user)
        self.create_widgets()

    def create_widgets(self):

        # Boton que abrira el Sidebar
        self.sidebar_button = tk.Button(self, text='☰', background='#B79C27', foreground='white',
                                    font=('Bold',20), border = 0, activebackground='#B79C27',
                                    activeforeground='white')
        self.sidebar_button.place(relx=0.025,rely=0.5, anchor='center')
        self.sidebar_button.config(command=self.open_bar)

        # Texto de "Hub"
        toggle_text = ttk.Label(self, text='Staff', background='#B79C27', foreground='white', font=("Dubai Medium", 20))
        toggle_text.place(relx=0.15,rely=0.5, anchor='center')

    def open_bar(self):
        self.bar.lift()
        self.bar.place(x=0,y=70)
        self.sidebar_button.config(command=self.close_bar, text='❎')

    def close_bar(self):
        self.bar.place_forget()
        self.sidebar_button.config(command=self.open_bar, text='☰')


class StaffSideBarFrame(tk.Frame):
    # En esta clase
    def __init__(self,parent,toggle_menu, home_frame, user):
         super().__init__(parent,width=200,height=530, background='#B79C27',
                         highlightbackground='white', highlightthickness=1)
         self.parent = parent
         self.toggle_menu = toggle_menu
         self.current_frame = home_frame
         self.user = user
         self.create_widgets()
         self.home_frame = home_frame
         self.library_frame = StaffLibraryFrame(self.parent,self.user)
         # aqui se definiran los frames que sean del staff 

    def create_widgets(self): # Todos los botones pue 

        home_button = tk.Button(self, text='Inicio     🏡', font=("Dubai Medium", 16), background='#B79C27', foreground='white',
                                 border = 0, activebackground='#B79C27', activeforeground='white')
        home_button.place(relx=0.13,rely=0.05)
        home_button.config(command=lambda: self.show_frame(self.home_frame))

        # Aqui iran los botones y widgets que correspondan a los frames del staff ############
        library_button = tk.Button(self, text='Bibilioteca', font=("Dubai Medium", 16), background='#B79C27', foreground='white',
                                    border = 0, activebackground='#B79C27', activeforeground='white')
        library_button.place(relx=0.13,rely=0.17)
        library_button.config(command=lambda: self.show_frame(self.library_frame))
        ######################################################################################
        
        logout_button = tk.Button(self, text='Cerrar Sesión🌏', font=("Dubai Medium", 16), background='#B79C27', foreground='white',
                                   border = 0, activebackground='#B79C27', activeforeground='white')
        logout_button.place(relx=0.13,rely=0.65)
        logout_button.config(command=self.log_out)

        exit_button = tk.Button(self, text='Salir    ❎', font=("Dubai Medium", 16), background='#B79C27', foreground='white',
                                 border = 0, activebackground='#B79C27', activeforeground='white')
        exit_button.place(relx=0.13,rely=0.77)
        exit_button.config(command=self.exit_app)
       
    def show_frame(self, frame):
        if self.current_frame:
            self.current_frame.place_forget()
        frame.place(relx=0.5,rely=0.556,anchor='center')  # Ajusta la posición según tus necesidades
        self.current_frame = frame
        self.toggle_menu.close_bar()

    def exit_app(self):
        sys.exit()

    def log_out(self):
        self.destroy()
        self.toggle_menu.destroy()
        self.library_frame.destroy()
        self.home_frame.destroy()
        self.toggle_menu.log_out_callback()