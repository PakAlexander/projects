from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
class Container(GridLayout):

    text_input = ObjectProperty()
    label_widget = ObjectProperty()

    def change_text(self):
        self.label_widget.text = self.text_input.text.upper()
class MyApp(App):
    def build(self):
        return Container()

if __name__ == '__main__':
    MyApp().run()
