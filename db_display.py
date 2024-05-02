# db_display
# handles database gui updates

import tkinter as tk
from tkinter import *
from xylempi_database import XylemPiDatabase

class DbDisplay:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.headers = ["ID", "Moisture", "Temperature", "Humidity", "Pressure", "Luminosity", "Irrigation Score", "Timestamp"]
        self.db_data = []
        self.col_width = None
        self.setup_gui()
        
        
    def setup_gui(self):
        self.db_window = tk.Toplevel(self.root)
        self.db_window.title("Historical Data Values")
        
        self.db_frame = tk.Frame(self.db_window)
        self.db_frame.grid(row=0, column=0, padx=10, pady=10)
        
        self.db_read_text = tk.Text(self.db_window, width=120, height=20)

        self.update_db_display() # initial display
        
        self.last_irrig_button = tk.Button(self.db_frame, text="Last \nIrrigation", command=lambda: self.update_db_display(self.db.get_latest_irrigation()))
        self.last_irrig_button.grid(row=0, column=0, padx=10, pady=10)
        
        self.default_last_25_button = tk.Button(self.db_frame, text="Last 25 Records \n(Default)", command=lambda: self.update_db_display(self.db.get_last_25_entries()))
        self.default_last_25_button.grid(row=0, column=1, padx=10, pady=10)
        
        self.all_records_button = tk.Button(self.db_frame, text="All Records \n(Caution!)", command=lambda: self.update_db_display(self.db.get_all_data()))
        self.all_records_button.grid(row=0, column=2, padx=10, pady=10)
        
        self.close_db_window_button = tk.Button(self.db_frame, text="Back to Main", command=self.close_db_window)
        self.close_db_window_button.grid(row=0, column=3, padx=10, pady=10)

    
        
    def update_db_display(self, data=None):
        print("from top of update_db_display")
        self.db_read_text.config(state=tk.NORMAL)
        self.db_read_text.delete("1.0", tk.END)
        
        if data is None:
            db_data = self.db.get_last_25_entries()
        else:
            db_data = [data]
            
            
        # display formatting:
        print(self.col_width)
        self.col_width = [max(len(str(header)), max(len(str(row[i])) if len(str(row[i])) > 0 else 0 for row in db_data)) for i, header in enumerate(self.headers)]
        print(self.col_width)
        #head_lin = " | ".join(header.ljust(width) for header, width in zip(self.headers, self.col_width))
        #separator = "-+-".join("-" * int(width) for width in self.col_width)
        head_lin = " | ".join(header.ljust(width) for header, width in zip(self.headers, self.col_width))
        separator = "-+-".join("-" * int(width) for width in self.col_width)
        self.db_read_text.insert(tk.END, separator + "\n")
        
        #insert rows
        for row in db_data:
            formatted_row = " | ".join(str(cell).ljust(width) for cell, width in zip(row, self.col_width))
            self.db_read_text.insert(tk.END, formatted_row + "\n")
        self.db_read_text.config(state=tk.DISABLED)
        self.db_read_text.grid(row=1, column=0, padx=20, pady=20)
                     
        
    def get_all_data(self):
        data = self.db.get_all_data()
        self.update_db_display(data)
    
    def get_last_25_entries(self):
        data = self.db.get_last_25_entries()
        self.update_db_display(data)
    
    def get_latest_irrigation(self):
        data = self.db.get_latest_irrigation()
        self.update_db_display(data)
    
    def close_db_window(self):
        self.db_window.destroy()