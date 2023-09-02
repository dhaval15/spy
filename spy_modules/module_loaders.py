import os, pathlib, sys
from importlib import util
import glob

ENV_FILE_NAME = '.spy.py'

def find_root_dir():
    cur_dir = os.getcwd()
    while True:
        file_path = os.path.join(cur_dir, ENV_FILE_NAME)
        if os.path.isfile(file_path):
            return cur_dir
        else:
            parent_dir = os.path.dirname(cur_dir)
            if cur_dir != parent_dir:
                cur_dir = parent_dir
            else:
                break

def load_module(path, module_dir):
    spec = util.spec_from_file_location(
        name='module',  
        location=path,
        submodule_search_locations=[
            # Add path lookup locations
            module_dir,
        ]
    )
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

