import os
import pandas as pd
import glob
import tkinter as tk
from tkinter import filedialog, messagebox

def convert_csv_to_xlsx(folder_path):
    folder_path = folder_path.strip('"')
    
    if not os.path.exists(folder_path):
        messagebox.showerror("Error", f"The folder path '{folder_path}' does not exist.")
        return
    
    csv_files = glob.glob(os.path.join(folder_path, '*.csv'))
    
    if not csv_files:
        messagebox.showinfo("Info", f"No CSV files found in the folder '{folder_path}'.")
        return

    for csv_file in csv_files:
        try:
            df = pd.read_csv(csv_file)
            xlsx_file = csv_file.replace('.csv', '.xlsx')
            df.to_excel(xlsx_file, index=False)
            print(f"Converted {csv_file} to {xlsx_file}")
        
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert {csv_file} due to: {e}")

    delete_choice = messagebox.askyesno("Delete CSVs", "Do you want to delete the original CSV files?")
    
    if delete_choice:
        for csv_file in csv_files:
            try:
                os.remove(csv_file)
                print(f"Deleted {csv_file}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete {csv_file} due to: {e}")
    else:
        messagebox.showinfo("Info", "CSV files were not deleted.")

def convert_xlsx_to_csv(folder_path):
    folder_path = folder_path.strip('"')
    
    if not os.path.exists(folder_path):
        messagebox.showerror("Error", f"The folder path '{folder_path}' does not exist.")
        return
    
    xlsx_files = glob.glob(os.path.join(folder_path, '*.xlsx'))
    
    if not xlsx_files:
        messagebox.showinfo("Info", f"No XLSX files found in the folder '{folder_path}'.")
        return

    for xlsx_file in xlsx_files:
        try:
            df = pd.read_excel(xlsx_file)
            csv_file = xlsx_file.replace('.xlsx', '.csv')
            df.to_csv(csv_file, index=False)
            print(f"Converted {xlsx_file} to {csv_file}")
        
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert {xlsx_file} due to: {e}")

def browse_folder_for_csv_to_xlsx():
    folder_path = filedialog.askdirectory()
    if folder_path:
        convert_csv_to_xlsx(folder_path)

def browse_folder_for_xlsx_to_csv():
    folder_path = filedialog.askdirectory()
    if folder_path:
        convert_xlsx_to_csv(folder_path)

# Create the main window
root = tk.Tk()
root.title("Acedia Slothy Tools")

# Set the size of the window
root.geometry("300x150")

# Add buttons for each functionality
button_csv_to_xlsx = tk.Button(root, text="CSV -> XLSX", command=browse_folder_for_csv_to_xlsx, padx=10, pady=10)
button_csv_to_xlsx.pack(pady=10)

button_xlsx_to_csv = tk.Button(root, text="XLSX -> CSV", command=browse_folder_for_xlsx_to_csv, padx=10, pady=10)
button_xlsx_to_csv.pack(pady=10)

# Start the main loop
root.mainloop()
