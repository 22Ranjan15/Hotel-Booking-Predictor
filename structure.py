import os 
from pathlib import Path

list_of_files = [
    ".gitignore",
    "requirements.txt",
    "setup.py",
    "config/__init__.py",
    "config/config.yaml",
    "config/paths_config.py",
    "config/model_params.py",
    "notebooks/experiments.ipynb",
    "src/__init__.py",
    "src/logger.py",
    "src/exception.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "pipeline/__init__.py",
    "pipeline/train_pipeline.py",
    "utils/__init__.py",
    "utils/utils.py",
    "static/style.css",
    "templates/index.html",
    "app.py",
    "README.md",
    "LICENSE",
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    if file_dir:
        os.makedirs(file_dir, exist_ok=True)

    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        with open(file_path, "w"):
            pass
    
# This code creates a project structure with the specified files and directories.