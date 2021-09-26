# Game
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import ObjectProperty
import random
from kivy.core.audio import SoundLoader

import lib

# Window.size = (720*0.5, 1280*0.5)

class GameWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed,self)
        self._keyboard.bind(on_key_down=self._on_key_down, on_key_up=self._on_key_up)

        tiles = [lib.entity.Tile(size=(50,50), source="assets/grass.png"),lib.entity.Tile(size=(50,50), source="assets/stone.png")]
        objects = [lib.entity.Object(),lib.entity.Object(size=(50,50), source="assets/bush.png"),lib.entity.Object(size=(50,50), source="assets/rock.png")]

        self.player = lib.entity.Player(size=(50,50), source="assets/player.png")
        self.map = lib.maps.MapLoader("map1.json", tiles=tiles, objects=objects)

        FPS = 60

        with self.canvas:
            self.draw()

        Clock.schedule_interval(self.update,1/FPS)


    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down, on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        self.player.keys_down(keycode[1])

    def _on_key_up(self, keyboard, keycode):
        self.player.keys_up(keycode[1])

    def draw(self):
        self.map.draw()
        self.player.draw()

    def update(self,dt):
        self.player.update()

    def on_touch_down(self, touch):
        super().on_touch_down(touch)

    def on_touch_up(self, touch):
        super().on_touch_up(touch)

    def on_touch_move(self, touch):
        super().on_touch_move(touch)


class MenuWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("app.kv")

class MyMainApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyMainApp().run()
