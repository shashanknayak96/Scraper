''' 
    A scrapper to scrap latest link of pool campus as posted on http://www.pvppcoe.ac.in/placement-notice 
    and email it.
'''

import requests
from bs4 import BeautifulSoup as bs
import os
import time
import smtplib

a = "abc"
while True:
    page = requests.get("http://www.pvppcoe.ac.in/placement-notice")
    soup = bs(page.content, 'html.parser')
    content = soup.find(class_="two_third first")
    main_content = content.select("table tbody tr")
    data = main_content[0]
    link = data.find('a')['href']
    title = data.find('a').get_text()
    date_1 = data.find_all('td')
    date_2 = date_1[1].get_text()
    file = open("test.txt", "r")
    a = file.read()
    if a == title:
        pass
    else:
        file.close()
        file = open("test.txt", "w")
        file.write(test)
        file.close()
        print("Sending mail...")
        smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpobj.ehlo()
        smtpobj.starttls()
        smtpobj.login(<YOUR_EMAIL>, <YOUR_PASSWORD>)       
        message = "Looks like I found a new link on the website!\nTitle: %s\nLink: %s\nDate: %s\n" % (link, title, date_2)
        smtpobj.sendmail(<YOUR_EMAIL>,<TO_ADDRESS>, msg=message)
        print("Mail sent!")
        smtpobj.quit()
    time.sleep(10) 

