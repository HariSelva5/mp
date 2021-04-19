import winsound
from win10toast import ToastNotifier
k=2
def timer (remider,seconds):
    notificator=ToastNotifier()
    notificator.show_toast("Reminder",f"""Alarm will go off in {seconds} Seconds.""",duration=k)
    notificator.show_toast(f"Reminder",remider,duration=k)

    #alarm
    frequency=5500
    duration=1000
    winsound.Beep(frequency,duration)

if __name__=="__main__":
    words="hi"#input("What would you remindes of: ")
    sec=2#int(input("Enter seconds: "))
    timer(words,sec)