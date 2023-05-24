from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size = (400, 800)
from kivy.config import Config

Config.set('kivy', 'keyboard_mode', 'systemanddock')


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

def get_ingr(m):
    nitro = str(10 * m / 1000)
    salt = str(15 * m / 1000)
    starts = str(0.5 * m / 1000)
    sugar= str(5 * m / 1000)
    salting_time = str(round(m / 500 * 2))
    return {'nitro': nitro, "salt": salt, "starts": starts, \
            "sugar": sugar, "time": salting_time}


class MyApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    MyApp().run()
