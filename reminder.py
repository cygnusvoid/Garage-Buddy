import winsound
from win10toast import ToastNotifier

#building reminder within a toast notification
def timer (reminder,seconds):
    toaster = ToastNotifier()

    toaster.show_toast(title = "Reminder", msg = "Alarm will go off in (seconds) seconds.", icon_path = "C:/Users/Hobbs/Downloads/GB-wrench.ico", duration = 10)
    toaster.show_toast(title = "Reminder", msg = reminder, icon_path = "C:/Users/Hobbs/Downloads/GB-wrench.ico", duration = 5)

#alarm sound, still within "timer" function
    frequency = 500
    duration = 1000
    winsound.Beep(frequency,duration)

#user input and calling "timer" function
if __name__ == "__main__":
    words = input ("What would you like to be reminded of? ")
    seconds = int(input("Enter seconds: "))

    timer (words, seconds)