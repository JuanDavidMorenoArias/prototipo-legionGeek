import sys
import tkinter as tk
from tkinter import ttk
from frames.home_page import HomeFrame
from frames.mileage_page import MileageFrame
from frames.stations_page import StationsFrame
from frames.vehicles_page import VehiclesFrame

class ToggleMenuFrame(tk.Frame):
    # En esta clase
    def __init__(self,parent, log_out_callback):
        super().__init__(parent,width=1000, background='orange',
                         highlightbackground='white', highlightthickness=1)    
        self.parent = parent
        self.log_out_callback = log_out_callback
        self.bar = SideBarFrame(self.parent,self)
        self.create_widgets()


    def create_widgets(self):

        # Boton que abrira el Sidebar
        self.sidebar_button = tk.Button(self, text='☰', background='orange', foreground='white',
                                    font=('Bold',20), border = 0, activebackground='orange',
                                    activeforeground='white')
        self.sidebar_button.place(relx=0.025,rely=0.5, anchor='center')
        self.sidebar_button.config(command=self.open_bar)

        # Texto de "Hub"
        toggle_text = ttk.Label(self, text='FuelTrack HUB', background='orange', foreground='white', font=("Dubai Medium", 20))
        toggle_text.place(relx=0.15,rely=0.5, anchor='center')

    def open_bar(self):
        self.bar.lift()
        self.bar.place(x=0,y=70)
        self.sidebar_button.config(command=self.close_bar, text='❎')

    def close_bar(self):
        self.bar.place_forget()
        self.sidebar_button.config(command=self.open_bar, text='☰')


# Para mayor comodidad seran dos clases en un mismo archivo ya que interactuan mucho entre ellas
class SideBarFrame(tk.Frame):
    # En esta clase
    def __init__(self,parent,toggle_menu):
         super().__init__(parent,width=200,height=530, background='orange',
                         highlightbackground='white', highlightthickness=1)
         self.parent = parent
         self.toggle_menu = toggle_menu
         self.current_frame = None
         self.create_widgets()
         self.home_frame = HomeFrame(self.parent)
         self.mileage_frame = MileageFrame(self.parent)
         self.stations_frame = StationsFrame(self.parent)
         self.vehicles_frame = VehiclesFrame(self.parent)

    def create_widgets(self): # Todos los botones pue 

        home_button = tk.Button(self, text='Home     🏡', font=("Dubai Medium", 16), background='orange', foreground='white',
                                 border = 0, activebackground='orange', activeforeground='white')
        home_button.place(relx=0.13,rely=0.05)
        home_button.config(command=lambda: self.show_frame(self.home_frame))

        mileage_button = tk.Button(self, text='Mileage  🕛', font=("Dubai Medium", 16), background='orange', foreground='white',
                                    border = 0, activebackground='orange', activeforeground='white')
        mileage_button.place(relx=0.13,rely=0.17)
        mileage_button.config(command=lambda: self.show_frame(self.mileage_frame))

        stations_button = tk.Button(self, text='Stations ⛽', font=("Dubai Medium", 16), background='orange', foreground='white',
                                     border = 0, activebackground='orange', activeforeground='white')
        stations_button.place(relx=0.13,rely=0.29)
        stations_button.config(command=lambda: self.show_frame(self.stations_frame))

        vehicles_button = tk.Button(self, text='Vehicles 🚙', font=("Dubai Medium", 16), background='orange', foreground='white',
                                     border = 0, activebackground='orange', activeforeground='white')
        vehicles_button.place(relx=0.13,rely=0.41)
        vehicles_button.config(command=lambda: self.show_frame(self.vehicles_frame))

        logout_button = tk.Button(self, text='Log out  🌏', font=("Dubai Medium", 16), background='orange', foreground='white',
                                   border = 0, activebackground='orange', activeforeground='white')
        logout_button.place(relx=0.13,rely=0.65)
        logout_button.config(command=self.log_out)

        exit_button = tk.Button(self, text='Exit      ❎', font=("Dubai Medium", 16), background='orange', foreground='white',
                                 border = 0, activebackground='orange', activeforeground='white')
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
        self.home_frame.destroy()
        self.mileage_frame.destroy()
        self.stations_frame.destroy()
        self.vehicles_frame.destroy()
        self.toggle_menu.log_out_callback()


