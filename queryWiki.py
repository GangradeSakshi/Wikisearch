from twilio.rest import TwilioRestClient
import searchWiki
import string
import re

ACCOUNT_SID = "AC0a23952dc53df0fde6667b272439b41b" 
AUTH_TOKEN = "2f2e7aa877cc3e5969cd859cdc1fbfc2" 
	 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

def getResult(client):
	query = "Abraham Lincoln"
	result = searchWiki.searchQuery(query)
	print result
	asciiResult = clean(result)
	firstSentence = asciiResult.split('.')[0]
	print firstSentence
	cleanResult = re.sub(r'/.*/', '', firstSentence)
	print cleanResult

	sendSMS(cleanResult)	

def sendSMS(result):
	# put your own credentials here 

	client.messages.create(
		to = "+16692369643",
		from_="+12057915894",
		body=result,
	)

def clean(s):
    return filter(lambda x: x in string.printable, s)	

if __name__=="__main__":
	getResult(client)
 



