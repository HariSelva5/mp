import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class MainWindow(Screen):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"
class WindowManager(ScreenManager):
    pass
# kv file
kv = Builder.load_file('insertcal.kv')
sm = WindowManager()
sm.add_widget(MainWindow(name='main'))
class HUT(App):
    def build(self):
        return sm
if __name__ == "__main__":
    HUT().run()


