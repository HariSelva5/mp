from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.widget import Widget
from kivy.storage.jsonstore import JsonStore
from kivy.uix.recycleview import RecycleView
from kivy.clock import Clock
from kivy.core.window import Window
Window.size = {300,500}


#form
class AddNewForm(Widget):
    text_input = ObjectProperty(None)

    input = StringProperty('')

    store = JsonStore("data.json")

    def submit_input(self):
        self.input = self.text_input.text
        print("Assign input: {}".format(self.input))
        self.save()
        self.input = ''
        sm.current='screen_home'

    def save(self):
        self.store.put(self.input)




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
kv = Builder.load_file('todo1.kv')

sm = WindowManager()



sm.add_widget(HomeScreen(name='screen_home'))
sm.add_widget(AddScreen(name='screen_add'))

# #app class
# class TodoApp(App):
#     pass
#     # def build(self):
#     #     return Menu()

# if __name__ == '__main__':
#     TodoApp().run()

 
class HUT(App):
    def build(self):
        return sm


# driver function
if __name__ == "__main__":
    HUT().run()
