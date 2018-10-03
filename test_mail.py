"""Example use of the pythonMail

This files tests the runtimes of each function within the mail module
aswell as logging the output to the ./logs directory.

"""

from PyMail import Gmail
from timeit import default_timer as timer
from MailLogging import debug

Gmail = Gmail()

def __main__():
	""" Runs all initialization code
	Returns:
		Dictionary: Contains all email information
	"""
	# Gets users total number of messages in all mailboxes
	msgTotal = Gmail.getUserInfo()['messagesTotal']

	start = timer()
	# Get list of `messageTotal` messages
	messages = Gmail.GetMessages().list(msgTotal)
	end = timer()
	print("Time to get ID's from Google:", end - start)

	start = timer()
	# Get list of raw messages
	rawMessage = Gmail.getMessageData(messages, format='raw', log=True)
	end = timer()

	start = timer()
	# Gets message data
	messageData = Gmail.getMessageData(messages, log=True)
	end = timer()
	print("Time to met message data from ID's:", end - start)

	start = timer()
	# Get payload of message data
	payloads = Gmail.getPayload(messageData, log=True)
	end = timer()
	print('Time to get payload from message data:', end - start)

	return payloads

def testMockData(payloads):
	"""Logs headers and body from payload

	writes data as an object to a json file located in ./logs, also logs
	all html/plain bodies as seperate .txt/.html files within the
	./logs/bodies directory.

	Args:
		payloads (dict): return of getPayload function
	"""
	start = timer()
	messageBodies = Gmail.unpackPayload(payloads, log=True)
	end = timer()
	print('Time to get message bodies:', end - start)

def testSend():
	"""Sends email based of user input"""
	mailData = [ input('Name: '), input('Recipient: '),
					input('Subject: '), input('content: ') ]

	start = timer()
	Gmail.sendMessage(*mailData)
	end = timer()
	print('Time to send an email:', end - start)

def testAll():
	"""Tests all functions"""
	payloads = __main__()
	testMockData(payloads)
	testSend()

if __name__ == '__main__':
	testAll()