#x = 5
#ts = 'The value of x is %s' %(x)
#print(ts)


import json
from pprint import pprint
import urllib2

eventKey=9159093

url = 'http://www.stubhub.com/ticketAPI/restSvc/event/%s' %(eventKey) # Update this url#

data = json.load(urllib2.urlopen(url))
tickets = data['eventTicketListing']['eventTicket']

priceIO = open('9159093_price.txt','a',1)

prices = [ticket['cp']for ticket in tickets]

for p in prices:
	pr = '%s' %(p)
	priceIO.write(pr+'\n')

priceIO.close()

#print(sorted(prices))

