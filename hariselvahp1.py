import pandas as pd
import random as r
import csv
from twilio.rest import Client
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


# # function for otp generation
# def otpgen():
#     otp=""
#     for i in range(4):
#         otp+=str(r.randint(1,9))
#     return ("Your OTP : {}".format(otp))
#     #print (otp)
# a=otpgen()




# # the following line needs your Twilio Account SID and Auth Token
# client = Client("AC6453d31f3bcee029abe3690c1954c32e", "09fc81ff544c86b6e3a6d892591affba")

# # change the "from_" number to your Twilio number and the "to" number
# # to the phone number you signed up for Twilio with, or upgrade your
# # account to send SMS to any phone number
# client.messages.create(to="+91-9043796669", 
#                        from_="+19284408533", 
#                        body=a)






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
    mobile = ObjectProperty(None)
    pwd = ObjectProperty(None)

    def validate(self):
        # validating if the email already exists
        users = pd.read_csv('loginhp.csv')
        if self.mobile.text not in users['Mobile'].unique():
            popFun()
        else:
            # switching the current screen to display validation result
            sm.current = 'homepage'
    # reset TextInput widget
            self.mobile.text = ""
            self.pwd.text = ""
    def forgotpassword(self):
        sm.current='otpmobile'
    def backbutton(self):
        sm.current='login'


#class for forgot password window
class forgotpasswordWindow(Screen):
    def backbutton(self):
        sm.current= 'login'


# class to accept sign up info
class signupWindow(Screen):
    name2 = ObjectProperty(None)
    mobile = ObjectProperty(None)
    pwd = ObjectProperty(None)

    def signupbtn(self):

        # creating a DataFrame of the info
        users = pd.read_csv('loginhp.csv')
        user = pd.DataFrame([[self.name2.text,  self.mobile.text, self.pwd.text]],
                            columns=['Name', 'Mobile', 'Password'])
        if self.mobile.text != "":
            if self.mobile.text not in users['Mobile'].unique():

                # if email does not exist already then append to the csv file
                # change current screen to log in the user now
                user.to_csv('loginhp.csv', mode='a', header=False, index=False)
                sm.current = 'login'
            self.name2.text = ""
            self.mobile.text = ""
            self.pwd.text = ""

        else:
            popFun()  # if values are empty or invalid show pop up

    def backbtn(self):
        sm.current = 'login'


#otp genration 
otp=""
for i in range(4):
    otp+=str(r.randint(1,9))
    A=otp


# class for otp verification
class logDataWindow(Screen):
    def writeotpcsv(self):
        with open('otphp.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            print(self.otp.text)
            # if self.otp.text != "":
            #     otp_value=self.otp.text
            #     print(otp_value)
    writeotpcsv()
    #onetimepwd is nothing but for going back
    def onetimepwd(self):
        sm.current= 'login'
    def verifybutton(self):
        sm.current= 'forgotpassword'
    def otpverification():
        print("a is {}".format(A))
    otpverification()
    # def writeotpcsv(self):
    #     with open('otphp.csv', 'w', newline='') as file:
    #         writer = csv.writer(file)
    #         if self.otp.text != "":
    #             otp_value=self.otp.text
    #             print(otp_value)
            #     writer.writerow(["otp"])
            #     writer.writerow([otp_value])
            #     sm.current = 'forgotpassword'
            #     self.otp.text = ""
            # else:
            #     popFun()  # if values are empty or invalid show pop up
    
            
                # B=self.otp.text
                # print(A,B)
                # if B==A:
                #     print("success")
                
               
            


  
    
        
        # def returnotp():
        #     return(A)
        # def otpformobile():
        #     return ("Your OTP : {}".format(A))
        # def sendotpmob():
        #     #the following line needs your Twilio Account SID and Auth Token
        #     client = Client("AC6453d31f3bcee029abe3690c1954c32e", "dd90f2c346993422fb2164983dbc927b")

        #     # change the "from_" number to your Twilio number and the "to" number
        #     # to the phone number you signed up for Twilio with, or upgrade your
        #     # account to send SMS to an#y phone number
        #     client.messages.create(to="+91-9043796669", 
        #                         from_="+19284408533", 
        #                         body=otpformobile())
        # sendotpmob()
    

    
# class for getting mobile number for sending an otp
class otpmobileWindow(Screen):
    def back(self):
        sm.current= 'login'
    def next(self):
        sm.current='logdata'
    def sendotp():
        sm.current='forgotpassword'
    

    # # the following line needs your Twilio Account SID and Auth Token
    # client = Client("AC6453d31f3bcee029abe3690c1954c32e", "09fc81ff544c86b6e3a6d892591affba")

    # # change the "from_" number to your Twilio number and the "to" number
    # # to the phone number you signed up for Twilio with, or upgrade your
    # # account to send SMS to any phone number
    # client.messages.create(to="+91-9043796669", 
    #                     from_="+19284408533", 
    #                     body=a)




#class for profile from homepage menu
class profileWindow(Screen):
    pass

#class for stats from homepage menu
class statsWindow(Screen):
    pass

#class for shared from homepage menu
class sharedWindow(Screen):
    pass

#class for trash from homepage menu
class trashWindow(Screen):
    pass

#class for settings from homepage menu
class settingsWindow(Screen):
    pass

#class for invitefriends from homepage menu
class invitefriendsWindow(Screen):
    pass

#class for contactus from homepage menu
class contactusWindow(Screen):
    pass

#class for settings from notification page
class notificationsettingsWindow(Screen):
    def backbtn(self):
        sm.current='notification'

#class for notification button from homepage
class notificationWindow(Screen):
    def noti_settings(self):
        sm.current = 'notifysettings'
    def backbutton(self):
        sm.current= 'homepage'

#class for settings option in wishlist window
class wishlistsettingsWindow(Screen):
    def backbtn(self):
        sm.current='wishlist'

#class for wishlist button from homepage
class wishlistWindow(Screen):
    def backbtn(self):
        sm.current='homepage'
    def wssettings(self):
        sm.current='wishlistsettings'

#class for chat button from homepage
class chatWindow(Screen):
    def backbtn(self):
        sm.current = 'homepage'
    def chatsettings(self):
        sm.current='chatsettings'
#class for settings option in chat window
class chatsettingsWindow(Screen):
    def backbtn(self):
        sm.current='chat'
    
#class for shopping lists from homepage
class shoppinglistsWindow(Screen):
    pass

#class for parties and events from homepage
class partiesandeventsWindow(Screen):
    pass

#class for calendar from homepage
class calendarWindow(Screen):
    pass

#class for bills from homepage
class billsWindow(Screen):
    pass

#class is for customizing dropdownmenu in the homepage
class CustomDropDown(DropDown):
    pass

# class for Homepage
class homepageWindow(Screen):
    def __init__(self, **kwargs):
        super(homepageWindow, self).__init__(**kwargs)
        self.dropdown = CustomDropDown()
        self.mainbutton = Button(text ='⚫ Menu  ',
                                 size_hint_x = 0.35, size_hint_y = 0.05, pos_hint ={'x':0.00, 'y':0.95},
                                     font_size='20',background_color=(0,0,0,0),color= [0,0,0,0.90],font_name= "verdana",bold= True)
        self.add_widget(self.mainbutton)
        self.mainbutton.bind(on_release = self.dropdown.open)
        self.dropdown.bind(on_select = lambda\
                           instance, x: setattr(self.mainbutton, 'text', x))
        self.dropdown.bind(on_select = self.callback)
    def callback(self, instance, x):
        if ( format ( x )== "profile"):
            sm.current= 'profile'
        elif( format ( x )== "stats"):
            sm.current= 'stats'
        elif( format ( x )== "shared"):
            sm.current= 'shared'
        elif( format ( x )== "trash"):
            sm.current= 'trash'
        elif( format ( x )== "settings"):
            sm.current= 'settings'
        elif( format ( x )== "invitefriends"):
            sm.current= 'invitefriends'
        elif( format ( x )== "contactus"):
            sm.current= 'contactus'
        else:
            '''x is self.mainbutton.text refreshed''' 
            print ( "The chosen mode is: {0}" . format ( x ) )
    def homebtn(self):
        sm.current='homepage'
    def wishlistbtn(self):
        sm.current='wishlist'
    def chatbtn(self):
        sm.current='chat'
    def notificationbtn(self):
        sm.current='notification'
    def shoppinglists(self):
        sm.current='shoppinglists'
    def partiesandevents(self):
        sm.current='partiesandevents'
    def calendar(self):
        sm.current='calendar'
    def bills(self):
        sm.current='bills'

    

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
sm.add_widget(otpmobileWindow(name='otpmobile'))
sm.add_widget(forgotpasswordWindow(name='forgotpassword'))
sm.add_widget(homepageWindow(name='homepage'))
sm.add_widget(profileWindow(name='profile'))
sm.add_widget(statsWindow(name='stats'))
sm.add_widget(sharedWindow(name='shared'))
sm.add_widget(trashWindow(name='trash'))
sm.add_widget(settingsWindow(name='settings'))
sm.add_widget(invitefriendsWindow(name='invitefriends'))
sm.add_widget(contactusWindow(name='contactus'))
sm.add_widget(notificationWindow(name='notification'))
sm.add_widget(wishlistWindow(name='wishlist'))
sm.add_widget(chatWindow(name='chat'))
sm.add_widget(shoppinglistsWindow(name='shoppinglists'))
sm.add_widget(partiesandeventsWindow(name='partiesandevents'))
sm.add_widget(calendarWindow(name='calendar'))
sm.add_widget(billsWindow(name='bills'))
sm.add_widget(notificationsettingsWindow(name='notifysettings'))
sm.add_widget(wishlistsettingsWindow(name='wishlistsettings'))
sm.add_widget(chatsettingsWindow(name='chatsettings'))



# class that builds gui


class HUT(App):
    def build(self):
        return sm


# driver function
if __name__ == "__main__":
    HUT().run()
