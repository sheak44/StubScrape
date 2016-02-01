#John Spaw
#Created 1/14/16

#Fetch raw data from StubHub
#Function will call for each individual event

import sys
import requests
import json
import csv
from time import time

def fetchEventData(eventID,eventName):

	#Event ID from StubHub
	event = str(eventID)
	
	#List holding each of the individual listing vectors
	tickets_list = []
	t = int(time())
	
	csvfile = eventName + '.csv'
	csvfields = ['location', 'row', 'qty', 'price']
	url = 'http://www.stubhub.com/ticketAPI/restSvc/event/' + event + '/sort/price/0?ts=' + str(t) + '000'
	
	print(url)
		
	#make get request to stubhub.com and take the result in json
	response = requests.get(url)
	response_dict = response.json()
	tickets = response_dict['eventTicketListing']['eventTicket']
	
	#Append individual listing values to a corresponding dictionary
	#Each listing will have its own dictionary which will all be contained in tickets_list
	for ticket in tickets:
		d = {}
		d['location'] = ticket['va']
		d['row'] = ticket['rd']
		d['qty'] = ticket['qt']
		d['price'] = ticket['cp']
		tickets_list.append(d)
		
	#io stream for csv file
	with open(csvfile, 'wb') as f:
		d_writer = csv.DictWriter(f, csvfields)
		d_writer.writer.writerow(csvfields)
		d_writer.writerows(tickets_list)
		
		
fetchEventData(9370538,'testData')