import time
from datetime import datetime as dt

hosts_temp = "website blocker/hosts.txt"
hosts_file = "/etc/hosts"
redirect = "127.0.0.1"
website_list = ["facebook.com", "www.facebook.com"]
current_time = dt.now().strftime("%H:%M:%S")
start = '10:00:00'
end = '12:00:00'

while True:
    if start < current_time < end:
        print("Working hours")
        with open(hosts_temp, 'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
                    
    else:
        print("Fun time")
        with open(hosts_temp, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                        file.write(line)
                file.truncate()
    time.sleep(10)
