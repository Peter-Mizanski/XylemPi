#gui.py
#this class deals with the tkinter gui

import tkinter as tk
from tkinter import *
from tkinter import ttk
from xylempi_database import XylemPiDatabase
from db_gui import DbGui


class GUI:
    #constructor
    def __init__(self, root):
        self.root = root
        self.moisture_frame = None
        self.temperature_frame = None
        self.humidity_frame = None
        self.pressure_frame = None
        self.timestamp_frame = None
        self.score_frame = None
        self.exit_frame = None
        self.irrigation_frame = None
        self.valve_frame = None
        self.db = XylemPiDatabase('xylempidb', 'pi', 'TetraData1!', 'localhost')
        self.setup_gui()
        
    def setup_gui(self):
        self.root.title("XylemPi: Plant Irrigation System")
        self.root.geometry("750x560")
        style = ttk.Style()
        style.theme_use("clam")
        
        #FRAMES
        self.timestamp_frame = tk.Frame(self.root, borderwidth=4,relief="groove", bg="#669999")
        self.timestamp_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        self.moisture_frame = tk.Frame(self.root, borderwidth=4, relief="groove", bg="#669999")
        self.moisture_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        
        self.luminosity_frame = tk.Frame(self.root, borderwidth=4, relief="groove", bg="#669999")
        self.luminosity_frame.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")
        
        self.temperature_frame = tk.Frame(self.root, borderwidth=4, relief="groove", bg="#669999")
        self.temperature_frame.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        
        self.humidity_frame = tk.Frame(self.root, borderwidth=4, relief="groove", bg="#669999")
        self.humidity_frame.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        
        self.pressure_frame = tk.Frame(self.root, borderwidth=4, relief="groove", bg="#669999")
        self.pressure_frame.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
        
        self.score_frame = tk.Frame(self.root, borderwidth=4, relief="groove", bg="#669999")
        self.score_frame.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")
        
        self.exit_frame = tk.Frame(self.root, borderwidth=4, relief="groove", bg="#996666")
        self.exit_frame.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        
        self.irrigation_frame = tk.Frame(self.root, borderwidth=4, relief="groove", bg="#CCFFCC")
        self.irrigation_frame.grid(row=0, column=1, rowspan=3, padx=5, pady=5, sticky="nsew")
        
        self.valve_frame = tk.Frame(self.root, borderwidth=4, relief="groove", bg="#CCFFCC")
        self.valve_frame.grid(row=3, column=1, rowspan=3, padx=5, pady=5, sticky="nsew")
        
        self.root.columnconfigure(0, weight=1)
        
        self.exit_button = tk.Button(self.exit_frame, text="Exit Program", font=("Impact", 14), command=self.exit_program)
        self.exit_button.grid(row=0, column=0, padx=7, pady=7)
        
        self.db_button = tk.Button(self.exit_frame, text="Historical Data", font=("Impact", 14), command=self.launch_db_display)
        self.db_button.grid(row=0, column=1, padx=7, pady=7)
        
        
    def launch_db_display(self):
        self.db_window = tk.Toplevel(self.root)
        self.db_window.title("Historical Data Values")
        self.db_gui = DbGui(self.db_window, self.db)
    
    def exit_program(self):
        self.root.destroy()