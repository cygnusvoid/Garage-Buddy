import winsound
from win10toast import ToastNotifier

#building reminder within a toast notification
def timer (reminder,seconds):
    toaster = ToastNotifier()

    toaster.show_toast(title = "Reminder", msg = "Alarm will go off in "+ str(seconds) + " minute(s).", icon_path = "C:/Users/Hobbs/Downloads/GB-wrench.ico", duration = seconds*60)
    toaster.show_toast(title = "Reminder", msg = reminder, icon_path = "C:/Users/Hobbs/Downloads/GB-wrench.ico", duration = 3)

#alarm sound, still within "timer" function
    frequency = 523
    duration = 500
    winsound.Beep(frequency,duration)
    frequency = 784
    duration = 200
    winsound.Beep(frequency,duration)
    frequency = 1047
    duration = 200
    winsound.Beep(frequency,duration)
    frequency = 523
    duration = 300
    winsound.Beep(frequency,duration)
    frequency = 523
    duration = 300
    winsound.Beep(frequency,duration)

#user input and calling "timer" function
if __name__ == "__main__":
    words = input ("What would you like to be reminded of? ")
    seconds = int(input("In how many minutes would you like to be reminded? "))

    timer (words, seconds)