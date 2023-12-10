from typing import Any

import none as none
from bs4 import BeautifulSoup, ResultSet
import requests
import schedule, sched, time as tym
from datetime import time, datetime, timedelta
import time
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

html_text = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')


def myFunc():
    for job in jobs:
        job_published_day = job.find('span', class_='sim-posted').span.text
        if 'few' in job_published_day:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            print(f"Company name: {company_name.strip()}")
            print(f"Required skills: {skills.strip()}")
            print(f"Post link: {more_info}")

            # print(job_published_day)
            # print('Company Name:', company_name,  'Skills required', skills, 'posted when', job_published_day)

scheduler.add_job(myFunc, 'interval', hours=6)

try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    pass
#schedule.every(1).minutes.do(myFunc)

# scheduler.enter(15, 1, myFunc, ())

# scheduler.run()

while True:
    schedule.run_pending()
    tym.sleep(2)

'''
with open('index.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    course_list = soup.find_all('li')
    for all_list in course_list:
        print(all_list.text)
    print(course_list)
#    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find('h3')
    print(tags)'''
