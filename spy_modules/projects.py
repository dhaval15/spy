import os
import glob

class Project:
    name: str
    parent: str
    path: str

    def __init__(self, name, parent, path):
        self.name = name
        self.parent = parent
        self.path = path

def project_from_env_file(file: str):
    path = os.path.dirname(file)
    parent = os.path.dirname(path)
    name = os.path.basename(path)
    return Project(name, parent, path)

def exclude(file: str):
    return file.startswith()

def find_projects(dir):
    env_files = glob.glob(f'{dir}/**/.spy.py')
    projects = list(map(project_from_env_file, env_files))
    return projects
