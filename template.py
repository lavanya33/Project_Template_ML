import os   #for creating files,folders
from pathlib import Path    #since we are creating files,folders under the project
import logging  #for errors


while True:
    project_name = input("Enter your project name: ")
    if project_name !='':
        break

logging.info(f"Creating project by name: {project_name}")

list_of_files = [
    ".github/workflows/.gitignore",
    ".github/workflows/main.yaml",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"config/config.yaml",
    "requirements.txt",
    "setup.py",
    "main.py",
    "schema.yaml",
    "README.md"
]  #contains the files,folders names needed for project


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating a new directory at : {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating a new file : {filename} for path {filepath} ")
    
    else:
        logging.info(f"file is already present at : {filepath}")