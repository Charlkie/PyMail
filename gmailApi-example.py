"""Simple Example of the gmail api library `pyMail`
"""

from PyMail import Gmail
from MailLogging import debug

Gmail = Gmail()

def main():

	# Gets users total number of messages in all mailboxes
	msgTotal = Gmail.getUserInfo()['messagesTotal']

	# example1	 # 	Get list of `messageTotal` messages  #  get list of messages (only id, no body nor subject))
	messages = Gmail.GetMessages().list(msgTotal)

	# example2
	messages2 = Gmail.GetMessages().list(msgTotal, ["INBOX"] ,'subject:("Welcome")')

	# example3   (only 5 messages)
	messages3 = Gmail.GetMessages().list(5, ["INBOX"] ,)


	####################       # in most cases you won't need to modify this block
	# Gets message data
	messageData = Gmail.getMessageData(messages, log=True)
	# Get payload of message data
	payloads = Gmail.getPayload(messageData, log=True)
	# Unpack payload
	messageBodies = Gmail.unpackPayload(payloads, log=True)
	####################
	

	for msg in messageBodies:  		 # printing messages bodies
		if 'html' in msg:        		 # simple check if it is html or text
			print(msg['html'])
		else:
			print(msg['plain'])



def testSend():
	"""Sends email based of user input"""
	mailData = [ input('Name: '), input('Recipient: '),
					input('Subject: '), input('content: ') ]

	Gmail.sendMessage(*mailData)



if __name__ == '__main__':
	main()
