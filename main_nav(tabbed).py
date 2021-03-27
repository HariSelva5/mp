from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder


class Test(TabbedPanel):
    pass


class TabbedPanelApp(App):
    def build(self):
        return Test()
    
kv = Builder.load_file('main_nav(tabbed).kv')


if __name__ == '__main__':
    TabbedPanelApp().run()