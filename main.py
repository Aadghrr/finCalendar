import requests as r
from bs4 import BeautifulSoup as bs 
import json
from datetime import datetime,timedelta

date = input("Enter date for events (yyyy-mm-dd): ")
date = datetime.strptime(date, '%Y-%m-%d')
to = date + timedelta(days=3)
to = strftime("%Y-%m-%d",to)
from = date - timedelta(days=3)
from = strftime("%Y-%m-%d",from)
size= str(100)
offset=str(0)


CALENDAR_BASE_URL = "https://finance.yahoo.com/calendar/earnings?from="+from+"&to="+to+"&day="+date+"&size="+size+"&offset="+offset 
DATA_ENTRY_POINT_STRING = "App.main = "
DATA_EXIT_POINT_STRING = ";\n}(this));\n</script>"


calendar = r.get(CALENDAR_BASE_URL)

soup = bs(calendar.content, 'html.parser')

html = list(soup.children)[1]
output = list(html.children)[1]
data = str(list(output.children)[2])

j = data[data.find(DATA_ENTRY_POINT_STRING) + len(DATA_ENTRY_POINT_STRING):data.find(DATA_EXIT_POINT_STRING)]

jsonData = json.loads(j)

#ScreenerCriteriaStore
#ScreenerResultsStore > results, fields
#StreamDataStore

upcomingEvents = jsonData['context']['dispatcher']['stores']['ScreenerResultsStore']['results']['rows']

print('Ticker | Company Name | Start Date | Time Type | EPS Estimate | EPS Actual | Quote Type')
print(10*'-')
for event in upcomingEvents:
    print(event['ticker'], ' ',event['companyshortname'],' ',event['startdatetime'],' ',event['startdatetimetype'],' ',event['epsestimate'],' ',event['epsactual'], ' ',event['quoteType'])


