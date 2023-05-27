from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivymd.uix.list import IRightBody, TwoLineAvatarIconListItem
class MainBox(MDBoxLayout):
    pass

class RightButton(IRightBody, MDIconButton):
    pass

class SearchResultItem(TwoLineAvatarIconListItem):
    pass

class BookPhoneApp(MDApp):
    def search_name(self, query):
        print(query)

    def search_number(self, query):
        print(query)

    def save_contact(self, user_name, user_phones):
        print(user_name, user_phones)

    def build(self):
        return MainBox()

if __name__ == '__main__':
    BookPhoneApp().run()

