from pythonMail import Gmail
from timeit import default_timer as timer
from MailLogging import debug
import re

def __main__():

	# Get list of 10 messages
	messages = Gmail.GetMessages().list(10)

	# Get list of raw messages
	#rawMessage = Gmail.getMessageData(messages, format='raw', log=True)

	# Gets message data
	messageData = Gmail.getMessageData(messages, log=True)

	# Get payload of messag data
	payloads = Gmail.getPayload(messageData, log=True)

	# Gets important headers from payload
	#Iheaders = Gmail.getImportantHeaders(payloads, log=True)

	debug.createLog(dir='logs/test')
	messageBodies = Gmail.getBody(payloads, log=True)

	# Get message test parts
	# start = timer()
	# body = Gmail.messageBody(payloads ,log=True)
	# end = timer()
	# print('Time of parts:', end - start)

	# Send a message
	# mailData = [
	# 	"Charl Kruger",
	# 	"charl.kruger@me.com",
	# 	"this is a cool and interesting subject",
	# 	"this is the content of that subject"
	# ]

	# Gmail.sendMessage(*mailData)

if __name__ == '__main__':
	__main__()
