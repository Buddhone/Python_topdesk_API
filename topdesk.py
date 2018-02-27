import requests, json, pprint
import csv
from datetime import date
from dateutil.relativedelta import relativedelta
from pandas.io.json import json_normalize
import sys


BASE_URL = 'http://topdesk_url/tas/api'
r = requests.get(BASE_URL + '/login/operator' , auth=('username', 'password'))

# Token to initiate the connection witht he API
TOKEN = r.text

# Format Token to be accepted by Topdesk API
TOKEN_ID = 'TOKEN id="' + TOKEN + '"'

#Call to previous month first and last day

today = date.today()
d = today - relativedelta(months=1)

first_day_previous_month = date(d.year, d.month, 1)
last_day_previous_month = date(today.year, today.month, 1) - relativedelta(days=1)

print(first_day_previous_month)
print(last_day_previous_month)

payload = {'creation_date_start':str(first_day_previous_month), 'creation_date_end':str(last_day_previous_month)}

# Topdesk API doesn't seem to accept changing the default number of retrieved incidents (10).
# Resorted to cicle through the incidents pages, to be reviewed.

incidents = requests.get(BASE_URL + '/incidents' + '?page_size={50}', headers={'Authorization': TOKEN_ID, 'Accept':'application/json'}, params=payload)
incidents2 = requests.get(BASE_URL + '/incidents' + '?start=10', headers={'Authorization': TOKEN_ID, 'Accept':'application/json'}, params=payload)
incidents3 = requests.get(BASE_URL + '/incidents' + '?start=20', headers={'Authorization': TOKEN_ID, 'Accept':'application/json'}, params=payload)
incidents4 = requests.get(BASE_URL + '/incidents' + '?start=30', headers={'Authorization': TOKEN_ID, 'Accept':'application/json'}, params=payload)
incidents5 = requests.get(BASE_URL + '/incidents' + '?start=40', headers={'Authorization': TOKEN_ID, 'Accept':'application/json'}, params=payload)
incidents6 = requests.get(BASE_URL + '/incidents' + '?start=50', headers={'Authorization': TOKEN_ID, 'Accept':'application/json'}, params=payload)
incidents7 = requests.get(BASE_URL + '/incidents' + '?start=60', headers={'Authorization': TOKEN_ID, 'Accept':'application/json'}, params=payload)
incidents8 = requests.get(BASE_URL + '/incidents' + '?start=70', headers={'Authorization': TOKEN_ID, 'Accept':'application/json'}, params=payload)
incidents9 = requests.get(BASE_URL + '/incidents' + '?start=80', headers={'Authorization': TOKEN_ID, 'Accept':'application/json'}, params=payload)

x = incidents.json()
x2 = incidents2.json()
x3 = incidents3.json()
x4 = incidents4.json()
x5 = incidents5.json()
x6 = incidents6.json()
x7 = incidents7.json()
x8 = incidents8.json()
x9 = incidents9.json()


file = open('jsonparsed.txt','w')
file.write(json.dumps(x, indent=4, sort_keys=True))
print(json.dumps(x, indent=4, sort_keys=True))
  
# Output to a csv file

with open('test.csv', 'w+') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
	spamwriter.writerow(['Call Number', 'call date', 'caller name'])
	for x in x:
		spamwriter.writerow([x["number"], x["callDate"], x["caller"]["branch"]["name"]])
	for x in x2:
		spamwriter.writerow([x["number"], x["callDate"], x["caller"]["branch"]["name"]])
	for x in x3:
		spamwriter.writerow([x["number"], x["callDate"], x["caller"]["branch"]["name"]])
	for x in x4:
		spamwriter.writerow([x["number"], x["callDate"], x["caller"]["branch"]["name"]])
	for x in x5:
		spamwriter.writerow([x["number"], x["callDate"], x["caller"]["branch"]["name"]])
	for x in x6:
		spamwriter.writerow([x["number"], x["callDate"], x["caller"]["branch"]["name"]])
	for x in x7:
		spamwriter.writerow([x["number"], x["callDate"], x["caller"]["branch"]["name"]])
	for x in x8:
		spamwriter.writerow([x["number"], x["callDate"], x["caller"]["branch"]["name"]])
	for x in x9:
		spamwriter.writerow([x["number"], x["callDate"], x["caller"]["branch"]["name"]])
