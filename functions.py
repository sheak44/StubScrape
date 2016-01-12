import json
from pprint import pprint
import urllib2
import time


####Create scrapeEvent function for creating single event vector file
####Turn event scrapes into a single function that returns a vector
####Restructure the way data is appended... add whole vectors at a time

def scrapePrice(eventKey):

	#Open IO stream with url
	url = 'http://www.stubhub.com/ticketAPI/restSvc/event/%s' %(eventKey)
	data = json.load(urllib2.urlopen(url))
	tickets = data['eventTicketListing']['eventTicket']
	
	#Open IO stream for sale vector file
	todayString = time.strftime("%d%m%Y")
	filename = '%s_%s_price.txt' %(eventKey,todayString)
	priceIO = open(filename,'a',1)
	
	#Create ordered array of prices
	prices = [ticket['cp']for ticket in tickets] 				#cp is a StubHub html attribute for base price
	print(sorted(prices))
	
	for p in prices:
		pr = '%s' %(p)
		priceIO.write(pr+'\n')
	
	priceIO.close()
	
	return prices
		
def scrapeQuantity(eventKey):

	#Open IO stream with url
	url = 'http://www.stubhub.com/ticketAPI/restSvc/event/%s' %(eventKey)
	data = json.load(urllib2.urlopen(url))
	tickets = data['eventTicketListing']['eventTicket']
	
	#Open IO stream for sale vector file
	todayString = time.strftime("%d%m%Y")
	filename = '%s_%s_quantity.txt' %(eventKey,todayString)
	priceIO = open(filename,'a',1)
	
	
	#Create array of ticket quantities
	quantities = [ticket['qt']for ticket in tickets] 			#qt is a StubHub html attribute for max sale quantity
	print(sorted(quantities))
		
	for q in quantities:
		qt = '%s' %(q)
		priceIO.write(qt+'\n')
		
	#Aggregate quantities... necessary?
	#totalQ = 0
	#for q in quantities:
	#	totalQ = totalQ + q		
	
	return quantities
	

eventKey = 9370534



scrapePrice(eventKey)
scrapeQuantity(eventKey)



	
