# import models
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton, MDFloatingActionButton, MDIconButton
from kivymd.uix.list import IRightBody, TwoLineAvatarIconListItem
from utils import phone_save, show_all_for_name, show_all_for_phone, show_all_phones, delete_by_id


class MainBox(MDBoxLayout):
    pass


class RightButton(IRightBody, MDIconButton):
    pass


class SearchResultItem(TwoLineAvatarIconListItem):
    def __init__(self, user_id, **kwargs):
        super(SearchResultItem, self).__init__(**kwargs)
        self.user_id = user_id
    def remove_contact(self):
        if delete_by_id(self.user_id):
            self.parent.remove_widget(self)

class BookPhoneApp(MDApp):
    def show_all(self):
        app = MDApp.get_running_app()
        search_result = app.root.ids.search_result
        search_result.clear_widgets()
        for contact in show_all_phones():
            print(contact)
            search_result.add_widget(SearchResultItem(text=contact[0], secondary_text=contact[1], user_id=contact[2]))

    def search_name(self, query):
        app = MDApp.get_running_app()
        search_result = app.root.ids.search_result
        search_result.clear_widgets()
        for contact in show_all_for_name(query):
            print(contact)
            search_result.add_widget(SearchResultItem(text=contact[0], secondary_text=contact[1], user_id=contact[2]))

    def search_number(self, query):
        app = MDApp.get_running_app()
        search_result = app.root.ids.search_result
        search_result.clear_widgets()
        for contact in show_all_for_phone(query):
            print(contact)
            search_result.add_widget(SearchResultItem(text=contact[0], secondary_text=contact[1], user_id=contact[2]))


    def save_contact(self, user_name, user_phones):
        if phone_save(user_name, user_phones):
            app = MDApp.get_running_app()
            sm = app.root.ids.bottom_nav
            sm.switch_tab('screen search')
        print(user_name, user_phones)

    def build(self):
        return MainBox()


if __name__ == '__main__':
    BookPhoneApp().run()
