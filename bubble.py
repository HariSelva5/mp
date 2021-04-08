# Program to Show how to create a switch 
# import kivy module    
import kivy  
       
# base Class of your App inherits from the App class.    
# app:always refers to the instance of your application   
from kivy.app import App 
     
# this restrict the kivy version i.e  
# below this kivy version you cannot  
# use the app or software  
kivy.require('1.9.0') 
  
# module consists the floatlayout  
# to work with FloatLayout first  
# you have to import it  
from kivy.uix.floatlayout import FloatLayout
  
# The Button is a Label with associated
# actions that are triggered
# when the button is pressed 
from kivy.uix.button import Button
  
# The Bubble widget is a form of menu or a
# small popup where the menu options
# are stacked either vertically or horizontally.
from kivy.uix.bubble import Bubble
  
# ObjectProperty is a specialized sub-class of the
# Property class, so it has the same
# initialisation parameters as it:
# By default, a Property always takes a default value[.]
from kivy.properties import ObjectProperty
   
  
# Create the Bubble class
# on which the .kv file is
class Cut_copy_paste(Bubble):
    pass
  
# Create the Layout Class
class BubbleDemo(FloatLayout):
   
    def __init__(self, **kwargs):
        super(BubbleDemo, self).__init__(**kwargs)
        self.but_bubble = Button(text ='Press to show bubble')
        self.but_bubble.bind(on_release = self.show_bubble)
        self.add_widget(self.but_bubble)
        self.bubb = Cut_copy_paste()
  
    # Defining the function to show the bubble
    def show_bubble(self, *l):
        self.add_widget(self.bubb)
              
# Create the App class
class BubbleApp(App):
    def build(self):
        return BubbleDemo()
  
# run the App
if __name__ == '__main__':
    BubbleApp().run()