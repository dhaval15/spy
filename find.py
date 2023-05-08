import os
from spy_modules.projects import  find_projects
from run import  SPY_MODULE_DIR

WHITE_LIST = [
    '/home/dhaval/Hive/projects',
    '/home/dhaval/.config',
]

if __name__ == '__main__':
    for dir in WHITE_LIST:
        projects = find_projects(dir)
        for project in projects:
            if not project.path.startswith(SPY_MODULE_DIR):
                #print(f'{project.name} > {project.parent}')
                print(project.path)
