import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
class CalculatorGridLayout(GridLayout):
     def calculate(self, calculation):
          if calculation:
               try:
                    self.display.text = str(eval(calculation))
               except Exception:
                    self.display.text = "Error"

class CalculatorApp(App):
     def build(self):
          return CalculatorGridLayout()
calculateApp = CalculatorApp()
calculateApp.run()