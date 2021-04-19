import pandas as pd
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.core.window import Window
Window.clearcolor =(1,1,1, 1)
#242/255, 242/255, 242/255, 1 halfwhite
Window.size = (300,500)

# class to accept user info and validate it
class loginWindow(Screen):
    pass

# class for managing screens
class windowManager(ScreenManager):
    pass

# kv file
kv = Builder.load_file('ch.kv')
sm = windowManager()

# reading all the data stored
users = pd.read_csv('loginhp.csv')



# class that builds gui


class HUT(App):
    def build(self):
        return sm


# driver function
if __name__ == "__main__":
    HUT().run()
