import json
from pprint import pprint
import urllib2

url = 'http://www.stubhub.com/ticketAPI/restSvc/event/9341277'

data = json.load(urllib2.urlopen(url))
tickets = data['eventTicketListing']['eventTicket']

prices = [ticket['tc']['amount'] for ticket in tickets]
pprint(sorted(prices))