import os
import argparse
from spy_modules.projects import  find_projects

WHITE_LIST = [
    '/home/dhaval/Hive/projects',
    '/home/dhaval/.config',
]

if __name__ == '__main__':
    argParser = argparse.ArgumentParser()
    argParser.add_argument('directory', nargs='?', default=None, help='Module directory')
    args = argParser.parse_args()
    for dir in WHITE_LIST:
        projects = find_projects(dir)
        for project in projects:
            if not project.path.startswith(args.directory):
                #print(f'{project.name} > {project.parent}')
                print(project.path)
