from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import (Color, Ellipse, Line, Rectangle)

from kivy.uix.button import Button
from kivy.core.window import Window
from random import random

class Painter(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            radius = 30
            Color(random(), random(), random())
            Ellipse(pos=(touch.x - radius / 2, touch.y - radius / 2), size=(radius, radius))
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=15)

    def on_touch_move(self, touch):
        touch.ud['line'].points += (touch.x, touch.y)


class MyApp(App):
    def build(self):
        painter = Widget()
        self.painter = Painter()
        painter.add_widget(self.painter)
        painter.add_widget(Button(text='Clear', on_press=self.clear_canvas, size=(100, 50)))
        painter.add_widget(Button(text='Save', on_press=self.save_canvas, size=(100, 50), pos=(100, 0)))
        painter.add_widget(Button(text='Screen', on_press=self.screen_canvas, size=(100, 50), pos=(200, 0)))
        return painter

    def screen_canvas(self, instance):
        Window.screenshot('screen.png')
    def clear_canvas(self, instance):
        self.painter.canvas.clear()

    def save_canvas(self, instance):
        self.painter.size = (Window.size[0], Window.size[1])
        self.painter.export_to_png('image.png')


if __name__ == '__main__':
    MyApp().run()
