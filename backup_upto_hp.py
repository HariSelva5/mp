import pandas as pd
import random as r
import csv
import pickle
import datetime
import os
from twilio.rest import Client
from kivy.base import runTouchApp
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.graphics import Line
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.uix.image import Image
from kivymd.theming import ThemeManager
from kivy.core.window import Window
Window.clearcolor =(1,1,1, 1) 
#242/255, 242/255, 242/255, 1 halfwhite
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
    mobile = ObjectProperty(None)
    pwd = ObjectProperty(None)

    def validate(self):
        # validating if the email already exists
        users = pd.read_csv('loginhp.csv')
        if self.username.text not in users['Name'].unique():
            popFun()
        else:
            # switching the current screen to display validation result
            sm.current = 'homepage'
    # reset TextInput widget
            self.username.text = ""
            self.pwd.text = ""
    def forgotpassword(self):
        sm.current='otpmobile'
    def backbutton(self):
        sm.current='login'


#class for forgot password window
class forgotpasswordWindow(Screen):
    username = ObjectProperty(None)
    mobile = ObjectProperty(None)
    confirmpwd = ObjectProperty(None)
    def backbutton(self):
        sm.current= 'login'
    def verify(self):
        if (self.newpwd.text and self.confirmpwd.text) != "":
            users = pd.read_csv('loginhp.csv')
            u=self.username.text
            n=self.newpwd.text
            c=self.confirmpwd.text
            index = users.index
            condition = users["Name"] == u
            idx = index[condition]
            idx_list = idx.tolist()
            users.at[idx_list, "Password"] = c
            if n!=c:
                popFun()
                self.confirmpwd.text=''
                self.newpwd.text=''
            else:
                users.to_csv('loginhp.csv', mode='w', header=True, index=False)
                self.username.text=''
                self.confirmpwd.text=''
                self.newpwd.text=''
                sm.current='login'        
        else:
            popFun()  # if values are empty or invalid show pop up  
       
        

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
with open('otphp.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["otp"])
    writer.writerow([A])
def otpformobile():
    return ("Your OTP : {}".format(A))

    
# class for otp verification
class logDataWindow(Screen):
    #onetimepwd is nothing but for going back
    def onetimepwd(self):
        sm.current= 'login'
    def verifybutton(self):
        otp_val=(self.onetimepassword.text)
        if otp_val==A:
            sm.current= 'forgotpassword'
        else:
            print("failure")
    
# class for getting mobile number for sending an otp
class otpmobileWindow(Screen):
    name2 = ObjectProperty(None)
     
        
    def sendotpmob(self):
        k=self.name2.text
        if k not in users['Name'].unique():
            popFun()  # if values are empty or invalid show pop up 
        else:    
               

            #the following line needs your Twilio Account SID and Auth Token
            client = Client("AC071b2848e866d06d7d91cabd1bda3a34", "3639203184b4d6e86a96b60d09b5d5a2")

            # change the "from_" number to your Twilio number and the "to" number
            # to the phone number you signed up for Twilio with
            client.messages.create(to="+91-6369683036", 
                                            from_="+12568417046", 
                                            body=otpformobile())
            sm.current='logdata'
            # self.name.text = "" 
    
    def back(self):
        sm.current= 'login'
    def next(self):
        sm.current='logdata'
    def sendotp():
        sm.current='forgotpassword'
    

#class for profile from homepage menu
class profileWindow(Screen):
    def backbtn(self):
        sm.current='homepage'


#class is for customizing dropdownmenu in the stats
class CustomDropDown(DropDown):
    pass
#class for stats from homepage menu
class statsWindow(Screen):
    def statlist(self):
        sm.current='statlist'
    def statbill(self):
        sm.current='statbill'
    def backbtn(self):
        sm.current='homepage'
class statlistWindow(Screen):
    pass
class statbillWindow(Screen):
    pass
#class for shared from homepage menu
class sharedWindow(Screen):
    def backbtn(self):
        sm.current='homepage'

#class for trash from homepage menu
class trashWindow(Screen):
    def backbtn(self):
        sm.current='homepage'

#class for settings from homepage menu
class settingsWindow(Screen):
    def backbtn(self):
        sm.current='homepage'

#class for invitefriends from homepage menu
class invitefriendsWindow(Screen):
    def backbtn(self):
        sm.current='homepage'

#class for contactus from homepage menu
class contactusWindow(Screen):
    def backbtn(self):
        sm.current='homepage'

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


    
#class for adding partiesandevents window
class partiesandeventsaddWindow(Screen):
    pass

#class for partiesandevents from homepage
class partiesandeventsWindow(Screen):
    def on_pre_enter(self):
        label= Label(text ="Parties and Events", font_size ='20sp',
            color =[0, 0, 0, 1],size_hint = (0.2, 0.1),
            pos_hint ={"x":0.4,"y":0.92})
        self.ids.float.add_widget(label)
        backbtn=Button(text='<',size_hint=(0.03,0.02),pos_hint ={"x":0.05,"y":0.96},
                        background_color =(0, 0, 0, 1),font_size="30",
				        color =(1, 1, 1, 1),bold=True)
        backbtn.bind(on_press=self.back) 
        self.ids.float.add_widget(backbtn)
        settings=Button(text='',size_hint=(0.03,0.02),pos_hint ={"x":0.93,"y":0.96} ,
                        background_normal= 'Settingsicon.png',
                        background_down= 'Settingsicon.png',mipmap= True)
        settings.bind(on_press=self.slsettings) 
        self.ids.float.add_widget(settings)
        button1=Button(text='+',size_hint=(.1,.1),pos_hint ={'x':.4, 'y':.0},
                        background_color =(0, 0, 0, 1),font_size="30",
				        color =(1, 1, 1, 1),bold=True)
        button1.bind(on_press=self.createnew)
        self.ids.grid.add_widget(button1)
    def createnew(self,event):
        btn = Button(text="New Note",size_hint=(.8,.1),pos_hint ={'x':.1, 'y':.65},
                        background_color =(0, 0, 0, 1),
				        color =(1, 1, 1, 1),bold=True) 
        btn.bind(on_press=self.addn) 
        self.ids.grid.add_widget(btn) 

    def addn(self, event):
        sm.current='partiesandeventsadd'
    def back(self,event):
        sm.current='homepage'
    def slsettings(self,event):
        sm.current='partiesandeventssettings'

    #here we have to make many lists first then go into the lists

#class for settings option in partiesandevents window
class partiesandeventssettingsWindow(Screen):
    def backbtn(self):
        sm.current='partiesandevents'
    
    
#class for adding shopping list window
class shoppinglistaddWindow(Screen):
    users=pd.read_csv('Book1.csv')
    print(users)
    def back(self):
        sm.current='shoppinglists'

#class for shopping lists from homepage
class shoppinglistsWindow(Screen):
    def on_pre_enter(self):
        #add button
        button1=Button(text='+',size_hint=(.1,.1),pos_hint ={'x':.4, 'y':.0},
                        background_color =(0, 0, 0, 1),font_size="30",
				        color =(1, 1, 1, 1),bold=True)
        button1.bind(on_press=self.createnew)
        self.ids.grid.add_widget(button1)
        #shopping list label
        label= Label(text ="Shopping Lists", font_size ='20sp',
            color =[0, 0, 0, 1],size_hint = (0.2, 0.1),
            pos_hint ={"x":0.4,"y":0.92})
        self.ids.float.add_widget(label)
        #back button
        backbtn=Button(text='<',size_hint=(0.03,0.02),pos_hint ={"x":0.05,"y":0.96},
                        background_color =(0, 0, 0, 1),font_size="30",
				        color =(1, 1, 1, 1),bold=True)
        backbtn.bind(on_press=self.back) 
        self.ids.float.add_widget(backbtn)
        #settings button
        settings=Button(text='',size_hint=(0.03,0.02),pos_hint ={"x":0.93,"y":0.96} ,
                        background_normal= 'Settingsicon.png',
                        background_down= 'Settingsicon.png',mipmap= True)
        settings.bind(on_press=self.slsettings) 
        self.ids.float.add_widget(settings)
    def createnew(self,event):
        btn = Button(text="New Note",size_hint=(.8,.1),pos_hint ={'x':.1, 'y':.65},
                        background_color =(0, 0, 0, 1),
				        color =(1, 1, 1, 1),bold=True) 
        btn.bind(on_press=self.addn) 
        self.ids.grid.add_widget(btn) 
    # def editnotename(self,event):
    #     on_release: root.select('profile')
    #def on_touch_down(self, touch):
        #if touch.is_double_tap:
            #print("hi")

    def addn(self, event):
        sm.current='shoppinglistadd'
    def back(self,event):
        sm.current='homepage'
    def slsettings(self,event):
        sm.current='shoppinglistsettings'

    #here we have to make many lists first then go into the lists

#class for settings option in shoppinglists window
class shoppinglistsettingsWindow(Screen):
    def backbtn(self):
        sm.current='shoppinglists'
    



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
                                     font_size='20',background_color=[0,0,0,0.90],color= (1,1,1,1),font_name= "verdana",bold= True)
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

#class for adding bills window
class billsaddWindow(Screen):
    pass



#class for bills from homepage
class billsWindow(Screen):
    def on_pre_enter(self):
        label= Label(text ="Bills", font_size ='20sp',
            color =[0, 0, 0, 1],size_hint = (0.2, 0.1),
            pos_hint ={"x":0.4,"y":0.92})
        self.ids.float.add_widget(label)
        backbtn=Button(text='<',size_hint=(0.03,0.02),pos_hint ={"x":0.05,"y":0.96},
                        background_color =(0, 0, 0, 1),font_size="30",
				        color =(1, 1, 1, 1),bold=True)
        backbtn.bind(on_press=self.back) 
        self.ids.float.add_widget(backbtn)
        settings=Button(text='',size_hint=(0.03,0.02),pos_hint ={"x":0.93,"y":0.96} ,
                        background_normal= 'Settingsicon.png',
                        background_down= 'Settingsicon.png',mipmap= True)
        settings.bind(on_press=self.slsettings) 
        self.ids.float.add_widget(settings)
        button1=Button(text='+',size_hint=(.1,.1),pos_hint ={'x':.4, 'y':.0},
                        background_color =(0, 0, 0, 1),font_size="30",
				        color =(1, 1, 1, 1),bold=True)
        button1.bind(on_press=self.createnew)
        self.ids.grid.add_widget(button1)
    def createnew(self,event):
        btn = Button(text="New Note",size_hint=(.8,.1),pos_hint ={'x':.1, 'y':.65},
                        background_color =(0, 0, 0, 1),
				        color =(1, 1, 1, 1),bold=True) 
        btn.bind(on_press=self.addn) 
        self.ids.grid.add_widget(btn) 

    def addn(self, event):
        sm.current='billsadd'
    def back(self,event):
        sm.current='homepage'
    def slsettings(self,event):
        sm.current='billssettings'

    #here we have to make many lists first then go into the lists

#class for settings option in bills window
class billssettingsWindow(Screen):
    def backbtn(self):
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
sm.add_widget(shoppinglistsettingsWindow(name='shoppinglistsettings'))
sm.add_widget(shoppinglistaddWindow(name='shoppinglistadd'))
sm.add_widget(partiesandeventssettingsWindow(name='partiesandeventssettings'))
sm.add_widget(partiesandeventsaddWindow(name='partiesandeventsadd'))
sm.add_widget(statlistWindow(name='statlist'))
sm.add_widget(statbillWindow(name='statbill'))
sm.add_widget(billssettingsWindow(name='billssettings'))
sm.add_widget(billsaddWindow(name='billsadd'))


# class that builds gui


class HUT(App):
    def build(self):
        return sm


# driver function
if __name__ == "__main__":
    HUT().run()
