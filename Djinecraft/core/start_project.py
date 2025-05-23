import os
import shutil
from importlib.resources import as_file, files


def start_project(project_name):
    project_root_path = os.path.join(os.getcwd(), project_name)

    if os.path.exists(project_root_path):
        print(f"Project '{project_name}' already exists.")
        return


    with as_file(files('Djinecraft.templates') / 'new_project') as template_dir:
        shutil.copytree(template_dir, project_root_path)


    os.rename(os.path.join(project_root_path, 'project'),
              os.path.join(project_root_path, project_name))

    print(f"Project '{project_name}' created at {project_root_path}")
