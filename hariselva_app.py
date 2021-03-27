import pandas as pd
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
Window.clearcolor = (0.55, 0.80, 0.50, 1)


# class to call the popup function
class PopupWindow(Widget):
    def btn(self):
        popFun()

# class to build GUI for a popup window


class P(FloatLayout):
    pass

# function that displays the content


def popFun():
    show = P()
    window = Popup(title="popup", content=show,
                   size_hint=(None, None), size=(300, 100))
    window.open()


# class to accept user info and validate it
class loginWindow(Screen):
    email = ObjectProperty(None)
    mobile = ObjectProperty(None)
    pwd = ObjectProperty(None)

    def validate(self):
        # validating if the email already exists
        users = pd.read_csv('loginhp.csv')
        if self.email.text not in users['Email'].unique():
            popFun()
        else:
            # switching the current screen to display validation result
            sm.current = 'homepage'
    # reset TextInput widget
            self.email.text = ""
            self.mobile.text = ""
            self.pwd.text = ""


# class to accept sign up info
class signupWindow(Screen):
    name2 = ObjectProperty(None)
    email = ObjectProperty(None)
    mobile = ObjectProperty(None)
    pwd = ObjectProperty(None)

    def signupbtn(self):
    
        # creating a DataFrame of the info
        users = pd.read_csv('loginhp.csv')
        user = pd.DataFrame([[self.name2.text, self.email.text, self.mobile.text, self.pwd.text]],
                            columns=['Name', 'Email', 'Mobile', 'Password'])
        if self.email.text != "":
            if self.email.text not in users['Email'].unique():

                # if email does not exist already then append to the csv file
                # change current screen to log in the user now
                user.to_csv('loginhp.csv', mode='a', header=False, index=False)
                sm.current = 'login'
            self.name2.text = ""
            self.email.text = ""
            self.mobile.text = ""
            self.pwd.text = ""

        else:
            popFun()  # if values are empty or invalid show pop up

    def backbtn(self):
        sm.current = 'login'


# class to display validation result
class logDataWindow(Screen):
    pass

# class for Homepage


class homepageWindow(Screen):
    pass

# class for managing screens


class windowManager(ScreenManager):
    pass


# kv file
kv = Builder.load_file('loginhp.kv')
sm = windowManager()

# reading all the data stored
users = pd.read_csv('loginhp.csv')

# adding screens
sm.add_widget(loginWindow(name='login'))
sm.add_widget(signupWindow(name='signup'))
sm.add_widget(logDataWindow(name='logdata'))
sm.add_widget(homepageWindow(name='homepage'))

# class that builds gui


class loginMain(App):
    def build(self):
        return sm


# driver function
if __name__ == "__main__":
    loginMain().run()
