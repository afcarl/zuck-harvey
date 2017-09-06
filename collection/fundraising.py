# https://www.facebook.com/zuck/posts/10103998949614711

from bs4 import BeautifulSoup
from time import sleep
import datetime
import random
from splinter import Browser
import pandas as pd

firefox_profile = '/Users/JosephNelson/Library/Application Support/Firefox/Profiles/ay779sfm.default'
url = 'https://www.facebook.com/zuck/posts/10103998949614711?pnref=story'

# make df
zuck_fund = pd.DataFrame(columns=['time','amount','shares'])

counter = 1534
done = False

while done == False:
    print('Yes1')
    with Browser('firefox', profile = firefox_profile) as browser:
        counter +=1
        print('Yes2')
        browser.visit(url) # open webpage 
        print('Yes3')
        sleep(5)
        print('Yes4')
        html = browser.html
        print('Yes5')
        soup = BeautifulSoup(html)
        print('Yes6')
        time = datetime.datetime.now()
        print('Yes7')
        amount = soup.find('span', {'class':'_191t _50f5'})
        print('RAISED ' + unicode(amount))
        shares = soup.find('a', {'class':'UFIShareLink'})
        print('Yes8')
        
        # add to df, export
        zuck_fund.loc[len(zuck_fund)]=[time, amount, shares]
        zuck_fund.to_csv('zuck_fund%d.csv'%counter, encoding='utf-8')
        
        # sleep
        sleeping = random.randint(60,90)
        print('Sleeping for %d'%sleeping)
        sleep(sleeping)