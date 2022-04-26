#Importing libraries
import schedule
import time

def job_that_executes_once():
    # Do some work that only needs to happen once...
    print ("test")

schedule.every(5).seconds.do(job_that_executes_once)

while True:
    schedule.run_pending()
    time.sleep(1)