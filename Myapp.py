from kivy.app import App
from KivyCalendar import CalendarWidget


class MyApp(App):

    def build(self):
        return CalendarWidget()

MyApp().run()