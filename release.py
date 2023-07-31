import os
import shutil


def load_configure():
  global ReleasePath
  config_file_name = os.path.splitext(
    os.path.basename(__file__))[0] + '_config.txt'
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
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(
      'Configuration File Created',
      f'A configuration file "{config_file_name}" has been created in the current directory.\nPlease edit the file and set the ReleasePath variable.'
    )
    ReleasePath = default_ReleasePath


def create_and_copy_files():
  # Get the current working directory of the Python script
  script_directory = os.getcwd()

  # Create the destination folder using ReleasePath
  destination_folder = os.path.join(script_directory, ReleasePath)

  # Check if the destination folder exists, and create it if it doesn't
  if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
    print(f"Created folder: {destination_folder}")

  # Replace 'source_folder_path' with the path of your source folder on your local system
  source_folder_path = "C:\ST_EXCEL\SearchTool_Sundar"

  # List the specific file paths to copy from the source folder
  files_to_copy = ["C:\ST_EXCEL\SearchTool_Sundar\t.bat"]
  for file_path in files_to_copy:
    if not os.path.isfile(file_path):
      print(f"Could not find {file_path} in the source folder.")
      continue

    file_name = os.path.basename(file_path)
    destination_file_path = os.path.join(destination_folder, file_name)

    # Copy the file to the destination folder
    try:
      shutil.copy(file_path, destination_file_path)
      print(f"Copied {file_path} to {destination_file_path}")
    except FileNotFoundError:
      print(f"Could not find {file_path}.")


if __name__ == "__main__":
  load_configure()
  create_and_copy_files()
