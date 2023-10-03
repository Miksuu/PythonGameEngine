import importlib.util

class FileManager():
    def __init__(self, file_path):
        self.file_path = file_path
        self.module = None

    def read_exec(self):
        with open(self.file_path, 'r') as file:
            code = file.read()
            exec(code, globals())
    
    def read_importlib(self):
        spec = importlib.util.spec_from_file_location("DynamicModule", self.file_path)
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)