from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory

KV_CODE = '''
RecycleView:
    viewclass: 'RVItem'
    RecycleBoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: self.minimum_height
        default_size_hint: 1, None
        default_size: 100, 30
        spacing: 10
        padding: 10
'''

class RVItem(Factory.Button):
    def get_data_index(self):
        return self.parent.get_view_index_at(self.center)
    @property
    def rv(self):
        return self.parent.recycleview
    def on_release(self):
        self.rv.data.pop(self.get_data_index())

class SampleApp(App):
    def build(self):
        return Builder.load_string(KV_CODE)
    def on_start(self):
        rv = self.root
        rv.data = ({'text': str(i), } for i in range(100))
SampleApp().run()