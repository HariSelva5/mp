from random import random
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line



class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        print(touch)

outer=MyPaintWidget()
class MainWindow(Screen):
    def paintbuild(self):
        return outer.on_touch_down()

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('paint1.kv')

sm = WindowManager()

sm.add_widget(MainWindow(name='main'))

# class that builds gui
class HUT(MDApp):
    def build(self):
       return sm

# driver function
if __name__ == "__main__":
    HUT().run()


