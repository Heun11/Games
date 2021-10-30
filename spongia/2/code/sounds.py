from kivy.core.audio import SoundLoader

# load sounds
SOUNDS = {
    "kick":SoundLoader.load("data/sounds/kick.wav"),
    "clap":SoundLoader.load("data/sounds/clap.wav")
}

class Sound:
    def __init__(self, tp, volume=0.1):
        self.sound = SOUNDS[tp]
        self.sound.volume = volume

    def play(self):
        self.sound.play()

    def stop(self):
        self.sound.stop()
        