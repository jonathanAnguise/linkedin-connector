class FileManager:

    def __init__(self):
        self.path = './url.txt'
        self.url_list = []

    def load_url(self):
        with open(self.path) as f:
            self.url_list = f.readlines()
