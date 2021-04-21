from kivy.app import App
import json
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.storage.jsonstore import JsonStore
from kivy.uix.recycleview import RecycleView
from kivy.clock import Clock
from kivy.factory import Factory
from kivy.core.window import Window
Window.size = {300,500}



class RVItem(Factory.Button):
    def on_release(self):
        sm.current='screen_add'



#form
class AddNewForm(Widget):
    item_input = ObjectProperty(None)
    title_input= ObjectProperty(None)
    input1 = StringProperty('')
    input2 = StringProperty('')

    store = JsonStore("data.json")

    def submit_input(self):
        self.input1 = self.title_input.text
        self.input2 = self.item_input.text
        self.store.put(self.input1, items=self.input2)
        self.title_input.text = ''
        self.item_input.text = ''
        sm.current='screen_home'

#recycle view for home screen
class MyRecycleView(RecycleView):

    def __init__(self, **kwargs):
        super(MyRecycleView, self).__init__(**kwargs)
        self.load_data()
        Clock.schedule_interval(self.load_data, 1)

    def load_data(self, *args):
        store = JsonStore("data.json")
        list_data = []
        for item in store:
            list_data.append({'text': item})

        self.data = list_data


# Declare both screens and manager
class HomeScreen(Screen):
    pass


class AddScreen(Screen):
    def __init__(self, **kwargs):
        super(AddScreen, self).__init__(**kwargs)
        self.addNewForm = AddNewForm()
        self.add_widget(self.addNewForm)





class WindowManager(ScreenManager):
    pass


# kv file
kv = Builder.load_file('todo2.kv')

sm = WindowManager()



sm.add_widget(HomeScreen(name='screen_home'))
sm.add_widget(AddScreen(name='screen_add'))



 
class HUT(App):
    def build(self):
        return sm


# driver function
if __name__ == "__main__":
    HUT().run()
