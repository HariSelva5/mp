from kivy.lang import Builder
from kivy.factory import Factory
from kivymd.app import MDApp
from kivymd.uix.list import IRightBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox

class ItemCheckBox(IRightBodyTouch, MDCheckbox):
    pass


class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "MyApp"
        self.theme_cls.primary_palette = "Blue"
        super().__init__(**kwargs)
    
    def add_item(self):
        new_item = self.root.ids.new_item.text
        self.root.ids.list_item.add_widget(Factory.ListItem(text=new_item))
        self.root.ids.new_item.text = ""

    def build(self):
        main_layout = Factory.MainLayout()
        items = []
        for item in items:
            main_layout.ids.list_item.add_widget(Factory.ListItem(text=item))
        
        self.root = main_layout

if __name__ == "__main__":
    MainApp().run()