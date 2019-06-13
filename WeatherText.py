""" Scrapes and parses the HTML on Wunderground """

from bs4 import BeautifulSoup
import requests
from twilio.rest import Client

# Account SID from twilio.com/console
account_sid = app.config['account_sid']
# Auth Token from twilio.com/console
auth_token  = app.config['auth_token']

client = Client(account_sid, auth_token)


""" Dallas Weather """

dal_url = 'https://www.wunderground.com/us/tx/dallas'
dal_webpage = requests.get(dal_url)
dal_soup = BeautifulSoup(dal_webpage.text, 'html.parser')

# Weather sentence at top of page - not live
dal_sentenceParse = dal_soup.findAll("div", {"data-station":"KTXDALLA339"})
for a in dal_sentenceParse:
    dal_Sentence = a.string

# Time of Sunset
dal_sunsetParse = dal_soup.findAll("span", {"id":"cc-sun-set"})
for b in dal_sunsetParse:
    dal_Sunset = b.string + "pm"
    dal_sunsetText = "Sunset is at " + dal_Sunset + "."

# Stage and Visibility of Moon
dal_moonParse = dal_soup.findAll("div", {"class":"moonNorth"})
for c in dal_moonParse:
    dal_Moon = c.getText().strip()
    dal_moonText = "The moon will be " + dal_Moon + "."

# High Temperature - not live
dal_highParse = dal_soup.findAll("div", {"class":"small-6 columns"})
for d in dal_highParse:
    dal_High = d.getText()

# Low Temperature - not live
dal_lowParse = dal_soup.findAll("strong", {"class":"low"})
for e in dal_highParse:
    dal_Low = e.string

# Current Time and Date
dal_dateParse = dal_soup.findAll("div", {"class":"local-time"})
for f in dal_dateParse:
    dal_Date = f.getText()

# Body of SMS message to be sent
#dal_bodyText = "It is" + dal_Date + ". Sunset is at " + dal_Sunset + " and the moon will be " + dal_Moon + "."


""" Atlanta Weather """

atl_url = 'https://www.wunderground.com/us/ga/atlanta'
atl_webpage = requests.get(atl_url)
atl_soup = BeautifulSoup(atl_webpage.text, 'html.parser')

atl_sunsetParse = atl_soup.findAll("span", {"id":"cc-sun-set"})
for b in dal_sunsetParse:
    atl_Sunset = b.string + "pm"
    atl_sunsetText = "Sunset is at " + atl_Sunset + "."

atl_moonParse = atl_soup.findAll("div", {"class":"moonNorth"})
for c in dal_moonParse:
    atl_Moon = c.getText().strip()
    atl_moonText = "The moon will be " + atl_Moon + "."

atl_dateParse = atl_soup.findAll("div", {"class":"local-time"})
for f in atl_dateParse:
    atl_Date = f.getText()

#atl_bodyText = "It is" + atl_Date + ". Sunset is at " + atl_Sunset + " and the moon will be " + atl_Moon + "."

#print(dal_bodyText)

# Generate and send SMS message. Add numbers from account.
#message = client.messages.create(
#    to="+1",
#    from_="+1",
#    body=body)
