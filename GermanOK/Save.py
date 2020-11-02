import json

class Save:
    """Data are stores in data.json
    There is a get, upload and download function to interact with the json file
    """
    
    def __init__(self,dico):
        self.dico = dico
        self.fileName = "data.json"
    
    def getDico(self):
        return self.dico
    
    def upload(self):
        with open(self.fileName, 'w') as file:
            file.write(json.dumps(self.dico))
        
    def download(self):
        with open(self.fileName,'r') as file:
            return json.loads(file.read())
