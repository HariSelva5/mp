from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.lang import Builder

Builder.load_file('scrolltest.kv')

class ExampleScreen(Screen):
    pass

sm = ScreenManager()

sm.add_widget(ExampleScreen(name = 'example'))

class TestApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()