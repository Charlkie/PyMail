from authentication import auth
from email.mime.text import MIMEText
from MailLogging import debug
import base64
import dateutil.parser as parser
import datetime
import os

"""
Gmail library to send and recieve information from a users mailbox using the Gmail api.
"""

class Gmail:

	def __init__(self):
		self.user_id = 'me'
		self.service = auth()
		debug.createLog()

	def getMessageData(self, messages, format=None, log=False):
		""" Return a list of message data in dictionary format """
		messages = [
			self.service.users().messages().get(userId=self.user_id, id=message['id'], format=format).execute()
			for message in messages['messages']
		]
		if log:
			debug.writeLog(format+' message' if format else 'messages', messages)
		return messages

	def getPayload(self, messages, log=False):
		""" Returns a list of payload data from message data """
		payloads = [ message['payload'] for message in messages ]
		if log:
			debug.writeLog('payload', payloads)
		return payloads

	def getImportantHeaders(self, payloads, log=False):
		""" Returns a list with Subject, Sender, Reciever, Time, Date from Payload data """
		IHeaders = []
		for payload in payloads:
			heads = {}
			header = payload['headers']
			for head in header:
				name = head['name']
				value = head['value']
				if name == 'Date':
					mail_date = str(parser.parse(value).date())
					today_date = str(datetime.datetime.today().strftime('%Y-%m-%d'))
					if mail_date == today_date:
						heads['dateTime'] = value[17:24]
					else:
						heads['dateTime'] = mail_date
				if name == 'Subject':
					heads['Subject'] = value
				if name == 'From':
					FROM, EMAIL = value.split('<')
					heads['From'] = FROM[:-1]
					heads['From-email'] = EMAIL[:-1]
			IHeaders.append(heads)
		if log:
			debug.writeLog('importantHeaders', IHeaders)
		return IHeaders

	def decodeMSG(self, message):
		msgString = base64.urlsafe_b64decode(message.encode('ASCII'))
		decoded = msgString.decode("utf-8")
		return decoded

	def getBody(self, messages, x=0, depth=0, types=['html', 'plain'], log=False, logdir):
		"""
		recurses through message parts untill it find the types specified,
		then returns the decoded part and appends it to a list/dictionary of
		all messages parts
		"""

		messageParts = []
		for msg in messages:
			type = msg['mimeType']
			# Plain text
			if type == 'text/plain' and 'plain' in types and depth == 0:
					body = self.decodeMSG(msg['body']['data'])
					messageParts.append(('plain',body))
			# Plain html
			elif type == 'text/html' and 'html' in types:
				body = self.decodeMSG(msg['body']['data'])
				messageParts.append(('html',body))
			# Plain text and html
			elif type == 'multipart/mixed' or type == 'multipart/alternative':
				msgParts = msg['parts']
				recurse = self.getBody(msgParts, x=x, depth=depth+1, types=types)
				messageParts.append(recurse[0])
			# Attatchment
			elif type == 'application/ics':
				pass
			x += 1

		if log:
			for (index, msg) in enumerate(messageParts):
				if msg[0] == 'html':
					debug.writeLog(str(index), msg[1], 'test/', extension="html")
				else:
					debug.writeLog(str(index), msg[1], 'test/', extension="txt")

		return messageParts

	class GetMessages:

		def __init__(self):
			self.service = auth()

		def list(self, results=1, labelIds=[]):
			""" Returns a list of messages and thread Id's for n number of messages """
			return self.service.users().messages().list(userId='me', labelIds=labelIds, maxResults=results).execute()

		def query(self, results=1, query=''):
			return self.service.users().messages().list(userId='me', q=query, maxResults=results).execute()

	def sendMessage(self, to, from_, subject, content):
		# create message base64 with MIMEText format
		created_message = self.createMessage(
			to,
			from_,
			subject,
			content
			)
		# send message
		message = (self.service.users().messages().send(userId="me", body=created_message).execute())

	def createMessage(self, sender, to, subject, message_text):
		message = MIMEText(message_text)
		message['to'] = to
		message['from'] = sender
		message['subject'] = subject
		return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

Gmail = Gmail()