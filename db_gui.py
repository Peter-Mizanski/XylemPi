#db_gui.py
# for database gui

import tkinter as tk
import csv
from tkinter import *

class DbGui:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.setup_gui()
        
    def setup_gui(self):        
        self.db_frame = tk.Frame(self.root, bg="#66CC99")
        self.db_frame.grid(row=1, column=0, padx=10, pady=10)
        
        self.button_frame = tk.Frame(self.root, bg="#66CCCC")
        self.button_frame.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        
        self.db_read_text = tk.Text(self.db_frame, width=120, height=20)
        self.headers = ["ID", "Moisture", "Temperature", "Humidity", "Pressure", "Luminosity", "Irrigation Score", "Timestamp"]
        
        self.update_db_display() #display init data
        
        self.search_button = tk.Button(self.button_frame, text="Last \nIrrigation",font=("Impact", 14), command=self.search_irrig_score, bg="#99FFCC")
        self.search_button.grid(row=0, column=0, padx=10, pady=10)
        
        self.recent_button = tk.Button(self.button_frame, text="Most Recent 10 Records \n(Default)", font=("Impact", 14), command=self.search_recent, bg="#999966")
        self.recent_button.grid(row=0, column=1, padx=10, pady=10)
        
        self.display_go_back = tk.Button(self.button_frame, text="All Records \n(Caution!)", font=("Impact", 14), command=self.search_all, bg="#FF9999")
        self.display_go_back.grid(row=0, column=2, padx=10, pady=10)
        
        self.export_csv_button = tk.Button(self.button_frame, text="Export \nData", font=("Impact", 14), command=self.export_data_to_csv, bg="#CCCCCC")
        self.export_csv_button.grid(row=0, column=3, padx=10, pady=10)
        
        self.exit_db_button = tk.Button(self.button_frame, text="Main \nMenu", font=("Impact", 14), command=self.root.destroy, bg="#CCCC99")
        self.exit_db_button.grid(row=0, column=4, padx=10, pady=10)
        
    def search_irrig_score(self):
        latest_irrig_score_30 = self.db.fetch_latest_irrig_score_30()
        if latest_irrig_score_30:
            self.update_db_display([latest_irrig_score_30]) # needed to wrap results in a list
        else:
            self.db_read_text.delete(tk.END, "\nNo rows found\n")
            
    def search_recent(self):
        recent_data = self.db.fetch_recent_data()
        if recent_data:
            self.update_db_display(recent_data)
        else:
            self.db_read_text.delete(tk.END, "\nNo rows found\n")
            
    def search_all(self):
        all_data = self.db.fetch_sensor_data()
        if all_data:
            self.update_db_display(all_data)
        else:
            self.db_read_text.delete(tk.END, "\nNo rows found\n")
    
    def update_db_display(self, data=None):
        self.db_read_text.delete("1.0", tk.END) # clear old data
        
        if data is None:
            db_data = self.db.fetch_recent_data()
        else:
            db_data = data
            
        # format data display
        column_widths = [max(len(str(header)), max(len(str(row[i])) for row in db_data)) for i, header in enumerate(self.headers)]
        header_line = " | ".join(header.ljust(width) for header, width in zip(self.headers, column_widths))
        self.db_read_text.insert(tk.END, header_line + "\n")
        separator_line = "-+-".join("-" * width for width in column_widths)
        self.db_read_text.insert(tk.END, separator_line + "\n")
        
        # insert data
        for row in db_data:
            formatted_row = " | ".join(str(cell).ljust(width) for cell, width in zip(row, column_widths))
            self.db_read_text.insert(tk.END, formatted_row + "\n")

        self.db_read_text.grid(row=1, column=0, padx=20, pady=20)
        
    def export_data_to_csv(self):
        data = self.db.fetch_sensor_data()
        
        if not data:
            self.db_read_text.insert(tk.INSERT, "No data!")
        else:
            self.db_read_text.insert(tk.INSERT, "\nData Exported Successfully!\n")
            
        self.db_read_text.update()
        
        #open a file and write to it
        with open('sensor_data.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.headers)
            writer.writerows(data)
            