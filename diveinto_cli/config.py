import json
import os.path

class Config:
    CONFIG_DIR = os.path.abspath(os.path.dirname(__file__))
    CONFIG_FILE = 'config.json'
    CONFIG_FILE_PATH = os.path.join(CONFIG_DIR, CONFIG_FILE)

    dic = {'LastTaskId':None}

    def __init__(self):
        if self.IsExistConfigFile():
            self.Load()
        else:
            self.Generate()

    def IsExistConfigFile(self):
        return os.path.isfile(self.CONFIG_FILE_PATH)

    def Load(self):
        with open(self.CONFIG_FILE_PATH, 'r') as f:
            self.dic = json.load(f)

    def Save(self):
        with open(self.CONFIG_FILE_PATH, 'w') as f:
            json.dump(self.dic, f)

    def Generate(self):
        with open(self.CONFIG_FILE_PATH, 'w') as f:
            json.dump(self.dic, f)
