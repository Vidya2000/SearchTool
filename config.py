import os
import tkinter as tk
from tkinter import messagebox

def load_configure():
    global ReleasePath
    config_file_name = os.path.splitext(os.path.basename(__file__))[0] + '_config.txt'
    config_file_path = os.path.join(os.getcwd(), config_file_name)

    if os.path.exists(config_file_path):
        # Configuration file exists, read the content
        with open(config_file_path, 'r') as file:
            ReleasePath = file.read().strip()
    else:
        # Configuration file doesn't exist, create it with default value
        default_ReleasePath = '<Enter location where you want to release>'
        with open(config_file_path, 'w') as file:
            file.write(default_ReleasePath)
        
        # Display a message box to prompt the user to fill up the configuration file
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo('Configuration File Created', f'A configuration file "{config_file_name}" has been created in the current directory.\nPlease edit the file and set the ReleasePath variable.')
        ReleasePath = default_ReleasePath

if __name__ == "__main__":
    load_configure()
    print(f'ReleasePath: {ReleasePath}')
