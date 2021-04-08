import pandas as pd
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.uix.image import Image
from kivymd.theming import ThemeManager
#from navigationdrawer import NavigationDrawer
#from kivy.garden.navigationdrawer import NavigationDrawer
from kivy.core.window import Window
Window.clearcolor = (0.55, 0.80, 0.50, 1)
Window.size = (300,500)


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



class CustomDropDown(DropDown):
    pass



# class for Homepage
class homepageWindow(Screen):
    
    def __init__(self, **kwargs):
        super(homepageWindow, self).__init__(**kwargs)
        self.dropdown = CustomDropDown()
        
        self.mainbutton = Button(text ='⚫ Menu  ',size_hint_x = 0.35, size_hint_y = 0.05, 
                                        pos_hint ={'x':0.00, 'y':0.95},font_size='20',
                                        background_color=(0,0,0,0),color= [0,0,0,0.90],
                                        font_name= "verdana",bold= True)



        self.btn1 = Button(text ="Profile",size_hint_x= None ,size_hint_y = None, height = 10)
        self.btn2 = Button(text ="Statistics",size_hint_x= None ,size_hint_y = None, height = 10)
        self.btn3 = Button(text ="Shared",size_hint_x= None ,size_hint_y = None, height = 10)
        self.btn4 = Button(text ="Trash",size_hint_x= None ,size_hint_y = None, height = 10)
        self.btn5 = Button(text ="Settings",size_hint_x= None ,size_hint_y = None, height = 10)
        self.btn6 = Button(text ="Invite Friends",size_hint_x= None ,size_hint_y = None, height = 10)
        self.btn7 = Button(text ="Contact Us",size_hint_x= None ,size_hint_y = None, height = 10)
        
        self.add_widget(self.btn1)
        self.btn1.bind(on_release = self.dropdown.open)
        self.dropdown.bind(on_select =self.profilebtn)

        self.add_widget(self.btn2)
        self.btn2.bind(on_release = self.dropdown.open)
        self.dropdown.bind(on_select =self.statsbtn)

        self.add_widget(self.btn3)
        self.btn3.bind(on_release = self.dropdown.open)
        self.dropdown.bind(on_select =self.sharedbtn)

        self.add_widget(self.btn4)      
        self.btn4.bind(on_release = self.dropdown.open)
        self.dropdown.bind(on_select =self.trashbtn)

        self.add_widget(self.btn5)
        self.btn5.bind(on_release = self.dropdown.open)
        self.dropdown.bind(on_select =self.settingsbtn)

        self.add_widget(self.btn6)
        self.btn6.bind(on_release = self.dropdown.open)
        self.dropdown.bind(on_select =self.invitefriendsbtn)

        self.add_widget(self.btn7)  
        self.btn7.bind(on_release = self.dropdown.open)
        self.dropdown.bind(on_select =self.contactusbtn)

        self.add_widget(self.mainbutton)
        self.mainbutton.bind(on_release = self.dropdown.open)
        self.dropdown.bind(on_select =self.onselect)

    
    def onselect(self, instance,x):
        print((self.mainbutton))
        sm.current = 'profilepage'
    
    def profilebtn(self, instance, x):
        sm.current = 'profilepage'
    def statsbtn(self, instance, x):
        sm.current = 'statspage'
    def trashbtn(self, instance, x):
        sm.current = 'trashpage'
    def sharedbtn(self, instance, x):
        sm.current = 'sharedpage'
    def settingsbtn(self, instance, x):
        sm.current = 'settingspage'
    def invitefriendsbtn(self, instance, x):
        sm.current = 'invitefriendspage'
    def contactusbtn(self, instance, x):
        sm.current = 'contactuspage'

    def notificationbtn(self):
        sm.current = 'notificationpage'
    def wsbtn(self):
        sm.current = 'wishlistpage'
    def chatbtn(self):
        sm.current = 'chatpage'
    def homebtn(self):
        sm.current = 'homepage'
    


# class to display notification window
class notificationWindow(Screen):
    pass

# class to display wishlist window
class wishlistWindow(Screen):
    pass
    

# class to display chat window
class chatWindow(Screen):
    pass


# class to display profile window
class profileWindow(Screen):
    pass

# class to display statistics window
class statsWindow(Screen):
    pass

# class to display shared window
class sharedWindow(Screen):
    pass


# class to display trash window
class trashWindow(Screen):
    pass

# class to display settings window
class settingsWindow(Screen):
    pass

# class to display invitefriends window
class invitefriendsWindow(Screen):
    pass

# class to display contactus
class contactusWindow(Screen):
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
sm.add_widget(notificationWindow(name='notificationpage'))
sm.add_widget(wishlistWindow(name='wishlistpage'))
sm.add_widget(chatWindow(name='chatpage'))
sm.add_widget(profileWindow(name='profilepage'))
sm.add_widget(statsWindow(name='statspage'))
sm.add_widget(sharedWindow(name='sharedpage'))
sm.add_widget(trashWindow(name='trashpage'))
sm.add_widget(settingsWindow(name='settingspage'))
sm.add_widget(invitefriendsWindow(name='invitefriendspage'))
sm.add_widget(contactusWindow(name='contactuspage'))


# class that builds gui


class HUT(App):
    def build(self):
        return sm


# driver function
if __name__ == "__main__":
    HUT().run()
