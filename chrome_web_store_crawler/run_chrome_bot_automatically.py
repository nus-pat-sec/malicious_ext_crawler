import schedule
import time
import datetime  
import subprocess

# def job(t):
#     print("I'm working...", t)
#     return

# schedule.every().day.at("15:35").do(job,'It is 01:00')

while True:
    # schedule.run_pending()
    # print("I'm working...",datetime.datetime.now())
    # time.sleep(5) # wait one minute
    print("Started program at", datetime.datetime.now(), file=open("log.txt", "a"))
    print("*Bot is working....", file=open("log.txt", "a"))


    result = subprocess.run(['scrapy', 'crawl', 'chrome_extensions'], stdout=subprocess.PIPE)
    print(result.stdout.decode('utf-8'))





    print("Finished the WHOLE process at", datetime.datetime.now(), file=open("log.txt", "a"))
    print("Started to wait 8 hours at", datetime.datetime.now(), file=open("log.txt", "a"))
    time.sleep(28800) #sleep for 8 hour then repeat

    print("\n", file=open("log.txt", "a"))

