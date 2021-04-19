from kivy.uix.button import Button
from kivymd.uix.picker import MDDatePicker
from kivy.lang import Builder

    
def show_date_picker(self):
    date_dialog = MDDatePicker()
    date_dialog.open()

