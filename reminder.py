import winsound
from win10toast import ToastNotifier

#building reminder within a toast notification
def timer (reminder,seconds):
    toaster = ToastNotifier

    toaster.show_toast ("Reminder", f """Alarm will go off in (seconds) seconds.""", duration = 20)
    toaster.show_toast (f"Reminder", reminder, duration = 20)