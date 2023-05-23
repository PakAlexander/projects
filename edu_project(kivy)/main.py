from kivy.app import App
from kivy.uix.gridlayout import GridLayout
# from kivy.properties import ObjectProperty
from kivy.core.window import Window
# from kivymd.textfields import MDTextField
# from kivymd.button import MDRaisedButton
from kivymd.theming import ThemeManager

from kivy.config import Config

Window.size = (720, 1280)
Config.set('kivy', 'keyboard_mode', 'systemanddock')
# Window.size = (400, 800)
def get_ingr(m):
    nitro = str(10 * m / 1000)
    salt = str(15 * m / 1000)
    starts = str(0.5 * m / 1000)
    sugar = str(5 * m / 1000)
    salting_time = str(round(m / 500 * 2))
    return {'nitro': nitro, "salt": salt, "starts": starts, "sugar": sugar, "time": salting_time}

class Container(GridLayout):
    def calculate(self):
        try:
            mass = int(self.text_input.text)
        except:
            mass = 0

        inridiets = get_ingr(mass)

        self.salt.text = inridiets.get('salt') + '5'
        self.solt_nitro.text = inridiets.get('nitro')
        self.starts.text = inridiets.get('starts')
        self.sugar.text = inridiets.get("sugar")
        self.time.text = inridiets.get("time")

class MyApp(App):
    theme_cls = ThemeManager()
    title = 'Coppa'
    def build(self):
        self.theme_cls.theme_style = 'Light'
        return Container()

if __name__ == '__main__':
    MyApp().run()
