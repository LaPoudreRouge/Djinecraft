from importlib.resources import files, as_file
import os
import shutil
import tempfile

def start_app(app_name):
    app_path = os.path.join(os.getcwd(), app_name)

    if os.path.exists(app_path):
        print(f"App '{app_name}' already exists.")
        return

    # Extract template files to a temp dir, then copy
    with as_file(files('Djinecraft.templates') / 'new_app') as app_template_dir:
        shutil.copytree(app_template_dir, app_path)

    print(f"App '{app_name}' created successfully.")
