import schedule
import time
import datetime  
import subprocess
# import string
# def job(t):
#     print("I'm working...", t)
#     return

# schedule.every().day.at("15:35").do(job,'It is 01:00')

while True:
    # schedule.run_pending()
    # print("I'm working...",datetime.datetime.now())
    # time.sleep(5) # wait one minute
    name_exported_file = '-name%s' % datetime.datetime.now().strftime('%Y%m%d%H:%M')
    print("Started program at", name_exported_file, file=open("log.txt", "a"))
    print("*Bot is working....", file=open("log.txt", "a"))

    result = subprocess.run(['scrapy', 'crawl', 'chrome_extensions', name_exported_file], stdout=subprocess.PIPE)
    print(result.stdout.decode('utf-8'))





    print("Finished the WHOLE process at", datetime.datetime.now(), file=open("log.txt", "a"))
    print("Started to wait 8 hours at", datetime.datetime.now(), file=open("log.txt", "a"))
    time.sleep(28800) #sleep for 8 hour then repeat

    print("\n", file=open("log.txt", "a"))

