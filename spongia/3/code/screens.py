from kivy.uix.screenmanager import Screen
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.clock import Clock

# Menu
class MenuScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        with self.canvas:
            Rectangle(size=(Window.size[0], Window.size[1]),source="data/images/menu_background.png", pos=(0,0))

# Game
class GameScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.FPS = 60
        self.screen_size = Window.size

    def on_enter(self, *args):
        super().on_enter(*args)
        Clock.schedule_interval(self.update,1/self.FPS)

    def update(self, dt):
        fps = int(1/dt)
        # UPDATE

        # DRAW
        self.canvas.clear()
        self.clear_widgets()
        with self.canvas:
            Rectangle()

        self.add_widget(Label(text=f"{fps}", pos_hint={"y":0.9}, size_hint=(0.1,0.1)))

    def on_touch_down(self, touch):
        super().on_touch_down(touch)

    def on_touch_move(self, touch):
        super().on_touch_move(touch)

    def on_touch_up(self, touch):
        super().on_touch_up(touch)
