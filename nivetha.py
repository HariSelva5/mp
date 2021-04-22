import kivymd
import csv
import datetime
import pandas as pd
import random as r
import calendar
import winsound
import emoji
from win10toast import ToastNotifier
from kivymd.uix.picker import MDTimePicker
from twilio.rest import Client
from kivymd.app import MDApp
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty
from kivymd.theming import ThemeManager
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.storage.jsonstore import JsonStore
from kivy.uix.recycleview import RecycleView
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = {300,500}

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


class MainWindow(Screen):
    
    mobile = ObjectProperty(None)
    pwd = ObjectProperty(None)

    def validate(self):
        # validating if the email already exists
        users = pd.read_csv('loginhp.csv')
        account=pd.read_csv('account.csv')
        if self.username.text=='' and self.pwd.text=='':
            if self.username.text not in users['Name'].unique():
                popFun()
        else:
            account=[self.pwd.text,self.username.text]
            csvfile = open('account.csv','w', newline='')
            obj = csv.writer(csvfile)
            obj.writerows(account)
            csvfile.close()
            # switching the current screen to display validation result
            sm.current = 'homepage'
    # reset TextInput widget
            self.username.text = ""
            self.pwd.text = ""
    def forgotpassword(self):
        sm.current='otpmobile'
    def backbutton(self):
        sm.current='login'
 
        
class RegisterWindow(Screen):
    name2 = ObjectProperty(None)
    mobile = ObjectProperty(None)
    pwd = ObjectProperty(None)

    def signupbtn(self):
        # creating a DataFrame of the info
        users = pd.read_csv('loginhp.csv')
        user = pd.DataFrame([[self.name2.text,  self.mobile.text, self.pwd.text]],
                            columns=['Name', 'Mobile', 'Password'])
        if self.mobile.text != "" and self.name2.text!=''and self.pwd.text!='':
            if self.mobile.text not in users['Mobile'].unique():

                # if email does not exist already then append to the csv file
                # change current screen to log in the user now
                user.to_csv('loginhp.csv', mode='a', header=False, index=False)
            self.name2.text = ""
            self.mobile.text = ""
            self.pwd.text = ""
            sm.current = 'main'
        else:
            popFun()  # if values are empty or invalid show pop up

    def backbtn(self):
        sm.current = 'main'

class ForgetpasswordWindow(Screen):
    username = ObjectProperty(None)
    mobile = ObjectProperty(None)
    confirmpwd = ObjectProperty(None)
    def backbutton(self):
        sm.current= 'main'
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
                sm.current='main'
        else:
            popFun()  # if values are empty or invalid show pop up



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
        sm.current= 'main'
    def verifybutton(self):
        otp_val=(self.onetimepassword.text)
        if otp_val==A:
            sm.current= 'forgetpassword'
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
            client = Client("AC071b2848e866d06d7d91cabd1bda3a34", "f1329791f96d513bd27f9ef97d563708")

            # change the "from_" number to your Twilio number and the "to" number
            # to the phone number you signed up for Twilio with
            client.messages.create(to="+91-6369683036",
                                            from_="+12568417046",
                                            body=otpformobile())
            sm.current='logdata'
            # self.name.text = ""

    def back(self):
        sm.current= 'main'
    def next(self):
        sm.current='logdata'
    def sendotp():
        sm.current='forgotpassword'


class HomepageWindow(Screen):
    def hp_settings(self):
        sm.current='homepagesettings'
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

#class for homepage settings window
class homepagesettingsWindow(Screen):
    def backbtn(self):
        sm.current='homepage'
    def account(self):
        sm.current= 'profile'
    def stats(self):
        sm.current= 'stats'
    def shared(self):
        sm.current= 'shared'
    def trash(self):
        sm.current= 'trash'
    def invitefriends(self):
        sm.current= 'invitefriends'
    def contactus(self):
        sm.current= 'contactus'



#class for profile from homepage menu
class profileWindow(Screen):
    def backbtn(self):
        sm.current='homepagesettings'
#class for stats from homepage menu
class statsWindow(Screen):
    def statlist(self):
        sm.current='statlist'
    def statbill(self):
        sm.current='statbill'
    def backbtn(self):
        sm.current='stats'
class statlistWindow(Screen):
    pass
class statbillWindow(Screen):
    pass
#class for shared from homepage menu
class sharedWindow(Screen):
    def backbtn(self):
        sm.current='homepagesettings'

#class for trash from homepage menu
class trashWindow(Screen):
    def backbtn(self):
        sm.current='homepagesettings'

#class for settings from homepage menu
class settingsWindow(Screen):
    def backbtn(self):
        sm.current='homepagesettings'

#class for invitefriends from homepage menu
class invitefriendsWindow(Screen):
    def backbtn(self):
        sm.current='homepagesettings'

#class for contactus from homepage menu
class contactusWindow(Screen):
    def backbtn(self):
        sm.current='homepagesettings'

#class for notification button from homepage
class notificationWindow(Screen):
    def noti_settings(self):
        sm.current = 'notifysettings'
    def backbutton(self):
        sm.current= 'homepage'

#class for settings from notification page
class notificationsettingsWindow(Screen):
    def backbtn(self):
        sm.current='notification'

#class for wishlist button from homepage
class WishlistWindow(Screen):
    def backbtn(self):
        sm.current='homepage'
    def wssettings(self):
        sm.current='wishlistsettings'

#class for settings option in wishlist window
class wishlistsettingsWindow(Screen):
    def backbtn(self):
        sm.current='wishlist'


#class for chat button from homepage
class ChatWindow(Screen):
    def backbtn(self):
        sm.current = 'homepage'
    def chatsettings(self):
        sm.current='chatsettings'
#class for settings option in chat window
class chatsettingsWindow(Screen):
    def backbtn(self):
        sm.current='chat'

#shopping lists starts

#form
class AddNewForm(Widget):
    text_input = ObjectProperty(None)

    input = StringProperty('')

    store = JsonStore("data.json")

    def submit_input(self):
        self.input = self.text_input.text
        print("Assign input: {}".format(self.input))
        self.save()
        self.input = ''
        sm.current='shoppinglists'

    def save(self):
        self.store.put(self.input)

#recycle view for home screen
class MyRecycleView(RecycleView):

    def __init__(self, **kwargs):
        super(MyRecycleView, self).__init__(**kwargs)
        self.load_data()
        Clock.schedule_interval(self.load_data, 1)

    def load_data(self, *args):
        store = JsonStore("data.json")
        list_data = []
        for item in store:
            list_data.append({'text': item})

        self.data = list_data

#class for shopping lists from homepage
class shoppinglistsWindow(Screen):
    def back(self):
        sm.current='homepage'
    def slsettings(self):
        sm.current='shoppinglistsettings'

#class for adding shopping lists
class shoppinglistaddWindow(Screen):
    def __init__(self, **kwargs):
        super(shoppinglistaddWindow, self).__init__(**kwargs)
        self.addNewForm = AddNewForm()
        self.add_widget(self.addNewForm)

#class for settings option in shoppinglists window
class shoppinglistsettingsWindow(Screen):
    def backbtn(self):
        sm.current='shoppinglists'


#form
class AddNewFormP(Widget):
    text_input = ObjectProperty(None)

    input = StringProperty('')

    store = JsonStore("dataP.json")

    def submit_input(self):
        self.input = self.text_input.text
        print("Assign input: {}".format(self.input))
        self.save()
        self.input = ''
        sm.current='partiesandevents'

    def save(self):
        self.store.put(self.input)

#recycle view for home screen
class MyRecycleViewP(RecycleView):

    def __init__(self, **kwargs):
        super(MyRecycleViewP, self).__init__(**kwargs)
        self.load_data()
        Clock.schedule_interval(self.load_data, 1)

    def load_data(self, *args):
        store = JsonStore("dataP.json")
        list_data = []
        for item in store:
            list_data.append({'text': item})

        self.data = list_data

#class for partiesandevents from homepage
class partiesandeventsWindow(Screen):
    def back(self):
        sm.current='homepage'
    def slsettings(self):
        sm.current='partiesandeventssettings'

#class for adding partiesandevents window
class partiesandeventsaddWindow(Screen):
    def __init__(self, **kwargs):
        super(partiesandeventsaddWindow, self).__init__(**kwargs)
        self.addNewFormP = AddNewFormP()
        self.add_widget(self.addNewFormP)

#class for settings option in partiesandevents window
class partiesandeventssettingsWindow(Screen):
    def backbtn(self):
        sm.current='partiesandevents'




#Daily expenses coding starts here

#form
class AddNewFormb(Widget):
    text_input = ObjectProperty(None)

    input = StringProperty('')

    store = JsonStore("datab.json")

    def submit_input(self):
        self.input = self.text_input.text
        print("Assign input: {}".format(self.input))
        self.save()
        self.input = ''
        sm.current='dailyexpenses'

    def save(self):
        self.store.put(self.input)

#recycle view for home screen
class MyRecycleViewb(RecycleView):

    def __init__(self, **kwargs):
        super(MyRecycleViewb, self).__init__(**kwargs)
        self.load_data()
        Clock.schedule_interval(self.load_data, 1)

    def load_data(self, *args):
        store = JsonStore("datab.json")
        list_data = []
        for item in store:
            list_data.append({'text': item})

        self.data = list_data

#class for dailyexpenses
class dailyexpensesWindow(Screen):
    def back(self):
        sm.current='homepage'
    def slsettings(self):
        sm.current='calculator'

#class for adding dailyexpenses
class dailyexpensesaddWindow(Screen):
    def __init__(self, **kwargs):
        super(dailyexpensesaddWindow, self).__init__(**kwargs)
        self.addNewFormb = AddNewFormb()
        self.add_widget(self.addNewFormb)

class WindowManager(ScreenManager):
    pass


# kv file
kv = Builder.load_file('hariselvakivymd.kv')

sm = WindowManager()



sm.add_widget(MainWindow(name='main'))
sm.add_widget(RegisterWindow(name='register'))
sm.add_widget(ForgetpasswordWindow(name='forgetpassword'))
sm.add_widget(logDataWindow(name='logdata'))
sm.add_widget(otpmobileWindow(name='otpmobile'))
sm.add_widget(HomepageWindow(name='homepage'))
sm.add_widget(homepagesettingsWindow(name='homepagesettings'))
sm.add_widget(profileWindow(name='profile'))
sm.add_widget(statsWindow(name='stats'))
sm.add_widget(statlistWindow(name='statlist'))
sm.add_widget(statbillWindow(name='statbill'))
sm.add_widget(sharedWindow(name='shared'))
sm.add_widget(trashWindow(name='trash'))
sm.add_widget(settingsWindow(name='settings'))
sm.add_widget(invitefriendsWindow(name='invitefriends'))
sm.add_widget(contactusWindow(name='contactus'))
sm.add_widget(notificationWindow(name='notification'))
sm.add_widget(notificationsettingsWindow(name='notifysettings'))
sm.add_widget(WishlistWindow(name='wishlist'))
sm.add_widget(wishlistsettingsWindow(name='wishlistsettings'))
sm.add_widget(ChatWindow(name='chat'))
sm.add_widget(chatsettingsWindow(name='chatsettings'))
sm.add_widget(shoppinglistsWindow(name='shoppinglists'))
sm.add_widget(shoppinglistaddWindow(name='shoppinglistadd'))
sm.add_widget(shoppinglistsettingsWindow(name='shoppinglistsettings'))
sm.add_widget(partiesandeventsWindow(name='partiesandevents'))
sm.add_widget(partiesandeventssettingsWindow(name='partiesandeventssettings'))
sm.add_widget(partiesandeventsaddWindow(name='partiesandeventsadd'))
sm.add_widget(dailyexpensesWindow(name='dailyexpenses'))
sm.add_widget(dailyexpensesaddWindow(name='dailyexpensesadd'))
sm.add_widget(calendarWindow(name='calendar'))
sm.add_widget(calendardateWindow(name='calendardate'))

# reading all the data stored
users = pd.read_csv('loginhp.csv')



# class that builds gui
class HUT(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        return sm


# driver function
if __name__ == "__main__":
    HUT().run()
























































 #self.theme_cls.primary_palette = "Teal"