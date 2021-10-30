import json

class MusicLoader:
    def load(index):
        with open("data/musics.json") as f:
            return json.load(f)[str(index)]

class Music:
    def __init__(self, code):
        self.code = code

    def run_code(self):
        pass

    def play(self):
        print("play=", self.code)

    def stop(self):
        print("stop=", self.code)