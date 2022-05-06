import winsound
from win10toast import ToastNotifier

#building reminder within a toast notification
def timer (reminder,seconds):
    toaster = ToastNotifier

    toaster.show_toast (title="Reminder", msg="Alarm will go off in (seconds) seconds.", icon_path=None , duration = 20)
    toaster.show_toast (f"Reminder", reminder, duration = 20)

#alarm sound, still within "timer" function
    frequency = 2500
    duration = 1000
    winsound.Beep(frequency,duration)

#user input and calling "timer" function
if __name__ == "__main__":
    words = input ("What would you like to be reminded of? ")
    seconds = int(input("Enter seconds: "))

    timer (words, seconds)