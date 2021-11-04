from kivy.core.audio import SoundLoader

class Sound:
    def __init__(self,path="", volume=0.1, loop=False):
        self.sound = SoundLoader.load(path)
        self.sound.volume = volume
        self.loop = loop

    def play(self):
        self.sound.play()
    
    def stop(self):
        self.sound.stop()