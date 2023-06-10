import os
from pathlib import Path
import logging

# Configure logging settings
logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]:%(message)s:')

# Define the project name
project_name = 'CNNClassifier'

# List of files to be created
List_of_files = [".github/workflows/.gitkeep",
                 f"src/{project_name}/__init__.py",
                 f"src/{project_name}/components/__init__.py",
                 f"src/{project_name}/utils/__init__.py",
                 f"src/{project_name}/config/__init__.py",
                 f"src/{project_name}/config/configuration.py",
                 f"src/{project_name}/pipeline/__init__.py",
                 f"src/{project_name}/entity/__init__.py",
                 f"src/{project_name}/constants/__init__.py",
                 "config/config.yaml",
                 "dvc.yaml",
                 "params.yaml",
                 "requirements.txt",
                 "setup.py",
                 "research/trials.ipynb",
                 "templates/index.html"
]


# Iterate over the list of files
for filepath in List_of_files:
    #Convert the file path to a 'Path' object
    filepath = Path(filepath)
    # Separate the file directory and the filename
    filedir, filename = os.path.split(filepath)
    
    # Create the directory if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create an empty file if it doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filename}")
    else:
        logging.info(f"{filename} already exists")