from kivy.app import App
import getdatecal
import winsound
from win10toast import ToastNotifier

from KivyCalendar import CalendarWidget
class MyApp(App):
    
    def build(self):
       
        def timer (remider,seconds):
            notificator=ToastNotifier()
            notificator.show_toast("Reminder",f"""Alarm will go off in {seconds} Seconds.""",duration=20)
            notificator.show_toast(f"Reminder",remider,duration=20)

            #alarm
            frequency=2500
            duration=1000
            winsound.Beep(frequency,duration)

        if __name__=="__main__":
            words=input("What would you remindes of: ")
            sec=int(input("Enter seconds: "))
            timer(words,sec)
        
        a=1
        if a==0:
            execfile('getdatecal.py')
       
      

MyApp().run()