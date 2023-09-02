import os
import argparse
from spy_modules.module_loaders import ENV_FILE_NAME, find_root_dir, load_module
from spy_modules.projects import  find_projects

def print_actions(config):
    for attr in dir(config):
        if callable(getattr(config, attr)) and attr.startswith('_') is False:
            print(attr)

if __name__ == '__main__':
    root_dir = find_root_dir()
    if root_dir is None:
        print('No .spy.py file found')
        print('run \'spy init\' in root directory of project to create .spy.py file')
        quit()
    env_file = os.path.join(root_dir, ENV_FILE_NAME)
    argParser = argparse.ArgumentParser()
    argParser.add_argument('directory', nargs='?', default=None, help='Module directory')
    argParser.add_argument('command', nargs='?', default='run', help='Sub command')
    args = argParser.parse_args()
    module = load_module(env_file, args.directory)
    options = {
        'root_dir': root_dir,
    }
    config = module.create_config(options)
    if args.command == 'current':
        print(root_dir)
        quit()
    if args.command == 'actions':
        print_actions(config)
        quit()
    command = getattr(config, args.command, None)
    if command is None:
        print(f"Subcommand: '{args.command}' not found")
        quit()
    print(f'Running {args.command}')
    command()
