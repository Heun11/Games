import os
# os.environ["KIVY_IMAGE"]="pil,sdl2"
import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string("""
<ExampleApp>:
    orientation: "vertical"
    Image:
        id: gif
        source: 'img.gif'
        center: self.parent.center
        size_hint: 1,1
        allow_stretch: True
        anim_delay: 0.10
        anim_loop: 0
""")

class ExampleApp(App, BoxLayout):
    def build(self):
        return self

if __name__ == "__main__":
    ExampleApp().run() 