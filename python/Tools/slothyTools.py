import os
import pandas as pd
import glob
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import subprocess
import sys

def install_missing_libraries():
    try:
        import pandas as pd
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
    try:
        import openpyxl
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "openpyxl"])

install_missing_libraries()

def convert_csv_to_xlsx(folder_path, console):
    folder_path = folder_path.strip('"')
    
    if not os.path.exists(folder_path):
        console.insert(tk.END, f"The folder path '{folder_path}' does not exist.\n\n")
        console.see(tk.END)
        return
    
    csv_files = glob.glob(os.path.join(folder_path, '*.csv'))
    
    if not csv_files:
        console.insert(tk.END, f"No CSV files found in the folder '{folder_path}'.\n\n")
        console.see(tk.END)
        return

    for csv_file in csv_files:
        try:
            df = pd.read_csv(csv_file, encoding='latin1')
            xlsx_file = csv_file.replace('.csv', '.xlsx')
            df.to_excel(xlsx_file, index=False)
            console.insert(tk.END, f"Converted {csv_file} to {xlsx_file}\n\n")
            console.see(tk.END)
        
        except Exception as e:
            console.insert(tk.END, f"Failed to convert {csv_file} due to: {e}\n\n")
            console.see(tk.END)

    delete_files_popup(console, csv_files)

def handle_delete_choice(console, files, delete_choice):
    if delete_choice == 'yes':
        for file in files:
            try:
                os.remove(file)
                console.insert(tk.END, f"Deleted {file}\n\n")
                console.see(tk.END)
            except Exception as e:
                console.insert(tk.END, f"Failed to delete {file} due to: {e}\n\n")
                console.see(tk.END)
    else:
        console.insert(tk.END, "Files were not deleted.\n\n")
        console.see(tk.END)

def convert_xlsx_to_csv(folder_path, console):
    folder_path = folder_path.strip('"')
    
    if not os.path.exists(folder_path):
        console.insert(tk.END, f"The folder path '{folder_path}' does not exist.\n\n")
        console.see(tk.END)
        return
    
    xlsx_files = glob.glob(os.path.join(folder_path, '*.xlsx'))
    
    if not xlsx_files:
        console.insert(tk.END, f"No XLSX files found in the folder '{folder_path}'.\n\n")
        console.see(tk.END)
        return

    for xlsx_file in xlsx_files:
        try:
            df = pd.read_excel(xlsx_file)
            csv_file = xlsx_file.replace('.xlsx', '.csv')
            df.to_csv(csv_file, index=False)
            console.insert(tk.END, f"Converted {xlsx_file} to {csv_file}\n\n")
            console.see(tk.END)
        
        except Exception as e:
            console.insert(tk.END, f"Failed to convert {xlsx_file} due to: {e}\n\n")
            console.see(tk.END)

    delete_files_popup(console, xlsx_files)

def browse_folder_for_csv_to_xlsx(console):
    folder_path = filedialog.askdirectory()
    if folder_path:
        convert_csv_to_xlsx(folder_path, console)

def browse_folder_for_xlsx_to_csv(console):
    folder_path = filedialog.askdirectory()
    if folder_path:
        convert_xlsx_to_csv(folder_path, console)

def delete_files_popup(console, files):
    delete_choice = messagebox.askyesno("Delete Files", "Do you want to delete the original files?")
    handle_delete_choice(console, files, 'yes' if delete_choice else 'no')

# Create the main window
root = tk.Tk()
root.title("Acedia Slothy Tools")

# Set the size of the window and make it resizable
root.geometry("600x300")
root.resizable(True, True)

# Add a frame for the buttons without a border
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Add buttons for each functionality side by side with an indication that they are clickable
button_csv_to_xlsx = tk.Button(button_frame, text="CSV -> XLSX", command=lambda: browse_folder_for_csv_to_xlsx(console), padx=10, pady=10)
button_csv_to_xlsx.pack(side=tk.LEFT, padx=5)

button_xlsx_to_csv = tk.Button(button_frame, text="XLSX -> CSV", command=lambda: browse_folder_for_xlsx_to_csv(console), padx=10, pady=10)
button_xlsx_to_csv.pack(side=tk.LEFT, padx=5)

# Add a scrolled text widget for the console output and make it expand to fill the window
console = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=600, height=15)
console.pack(pady=10, fill=tk.BOTH, expand=True)

# Disable direct typing in the console initially
console.bind("<Key>", lambda e: "break")

# Start the main loop
root.mainloop()