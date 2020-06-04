import subprocess, schedule, time, sys, datetime

#Function for execution, job MUST be callable
def execution():
        subprocess.check_output(command,shell=True)
        print("Job Done at {}".format(datetime.datetime.now()))
        return


#Function for Minutes
def minutes(minutes):
        schedule.every(int(minutes)).minutes.do(execution)
        
        while True:
                schedule.run_pending()
                time.sleep(1)


#Functions for Hours
def hours(hours):
        schedule.every(int(hours)).hour.do(execution)
        
        while True:
                schedule.run_pending()
                time.sleep(1)


#Funtion for Days
def days(days):
        
        schedule.every(int(days)).day.do(execution)
        
        while True:
                schedule.run_pending()
                time.sleep(1)


#Funtion for Months
def months(months):
        
        schedule.every(int(months)).months.do(execution)
        
        while True:
                schedule.run_pending()
                time.sleep(1)


#Controller
def controller(time,amount):
        if time == "mi":
                minutes(amount)
        elif time == "h":
                hours(amount)
        elif time == "d":
                days(amount)
        elif time == "m":
                months(amount)
        return;


#Main Function
try:
	command = sys.argv[3]
	controller(sys.argv[1],sys.argv[2])
except:
       print("python3 autom8.py [mi,m,h,d][amount in days/hours/months][command]")