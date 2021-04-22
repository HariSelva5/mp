from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.graphics import Line, Color
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup

from threading import Thread
from kivy.lang.builder import Builder

class MenuPopup(Popup):
  pass


#Builder.load_file('menuwidget.kv')

class StandardButton(Button):
    """
    Class for normal buttons
    """
    pass


class Container(BoxLayout):
    """
    kivy app main container as BoxLayout
    """
    global q
    line_size = NumericProperty()
    color = ListProperty([0, 0, 0, 1])
    tool_mode=StringProperty("pencil")

    action_text = StringProperty()
    def __init__(self, **kwargs):
        super(Container, self).__init__(*kwargs)
        self.action_text = str(". . .")

    def select_color(self, *args):
        """
        Opens popup window with color picker widget for user to select color.
        Selected color is set to working color of Lightrift.
        """
        color_wheel = ColorPopup().open()


class CanvasPaintWidget(Widget):
    """
     kivy Widget
    """
    global q

    def __init__(self, **kwargs):
        super(CanvasPaintWidget, self).__init__(**kwargs)
        self.is_popup_open=False
        self.line_size=4
        self.tool_mode='pencil'
        self.color = [0, 0, 0, 1]

    def set_line_size(self, new_size):
        """
        Set the working line width/size of Lightrift. Int
        """
        self.line_size = new_size

    def set_mode(self, new_mode):
        """
        Set the working mode of Lightrift. (lines, curves, erase, etc.) Stored
        as string
        """
        self.tool_mode = new_mode

    def set_color(self, new_color):
        """
        Set the working color of Lightrift. Sequence/list of 4 doubles (RGBA).
        """
        print("new color = " + str(new_color))
        self.color = new_color



    def dimiss_pop_up(self):
      popup.dismiss
      self.is_popup_open=False

    def on_touch_down(self, touch):
        print(touch)
        print(self.tool_mode)
        if touch.button == 'right':
          self.is_popup_open=True
          self.show_context_menu(touch)
        with self.canvas:
            if self.tool_mode == 'eraserdown':
               Color(1, 1, 1, 1)
            else:
              Color(*self.color, mode='rgba')
              print(self.line_size)
            touch.ud["line"] = Line(points=(touch.x, touch.y), width=self.line_size	)

    def on_touch_move(self, touch):
        touch.ud["line"].points += (touch.x, touch.y)

    def on_touch_up(self, touch):
        self.export_to_png('a' + '.png')

    def show_context_menu(self,touch):

      the_popup = MenuPopup()
      the_popup.open()
      #saveButton.bind(on_press = self.dimiss_pop_up)

class BoardPref(BoxLayout):
    pass

class ColorPopup(Popup):
    """
    Popup for the color picker wheel.
    """
    pass

class MenuPopup(Popup):
    pass

class CanvasPaintApp(App):
    def build(self):
        parent = Widget()
        self.painter = CanvasPaintWidget()
        parent.add_widget(self.painter)
        return Container()

    def clear_canvas(self, obj):
        self.painter.canvas.clear()

    def save(self, instance):
        #self.painter.size = (Window.size[0], Window.size[1])
        self.painter.export_to_png('image.png')

    def screen(self, instance):
        Window.screenshot('screen.png')

    def on_pause(self):
        """
        application switched
        """
        pass
        #return True


if __name__ == "__main__":

    Window.fullscreen = 0
    Window.show_cursor = 1
    Window.clearcolor = (1., 1., 1., 1.)

    CanvasPaintApp().run()

