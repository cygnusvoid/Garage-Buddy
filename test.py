#Importing libraries
import schedule
import time

def job_that_executes_once():
    # Do some work that only needs to happen once...
    print ("test")

schedule.every().day.at('21:26').do(job_that_executes_once)

while True:
    schedule.run_pending()
    time.sleep(1)
    break