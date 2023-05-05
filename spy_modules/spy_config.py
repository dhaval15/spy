import os

class SpyConfig:
    root_dir: str
    def __init__(self, options):
        self.root_dir = options['root_dir']

    def run(self, command):
        print(f'Running command: {command}')
        os.system(command)

    def edit(self):
        config = self.editor_config()
        args = f'-c \'luafile {config}\'' if self.check_path(config) else ''
        self.run(f'vim {args}')

    def editor_config(self):
        return os.path.join(self.root_dir, '.spy.lua')

    def check_path(self, path):
        return os.path.isfile(path)

    def assert_path(self, path):
        if self.check_path(path):
            return
        else:
            print(f'\'{path}\' does not exist')
            quit()
