from pymongo import MongoClient
from flask import Flask
from flask_graphql import GraphQLView
from Server.inputs import MessagesInput
from Server.schemas import MessagesSchema
from PyMail import Gmail
import graphene
from flask_cors import CORS
import json
from authentication import auth

Gmail = Gmail()

client = MongoClient('mongodb://test:test123@ds255332.mlab.com:55332/mailatschool')

app = Flask(__name__)
CORS(app)
db = client.mailatschool

messages = db['messages']

@app.route('/')
def index():
	return "Graph QL"

@app.route('/delete')
def deleteMail():
	messages.drop()
	print("all messages deleted")
	return "Deleted all messages"

@app.route('/debug')
def debug():
	Gmail.getUserInfo()['messagesTotal']
	return 'Bugs suck!'

@app.route('/addmail')
def addMail():
	unsavedMessages = Gmail.getUserInfo()['messagesTotal'] - messages.count()
	print(unsavedMessages)
	messages_ = Gmail.GetMessages().list(unsavedMessages)
	messageData = Gmail.getMessageData(messages_, log=False)
	payloads = Gmail.getPayload(messageData, log=False)
	parts = Gmail.getEverything(payloads, log=False)
	# parts = json.load(open('bodies.json'))
	# print("Length of parts", len(parts))
	for part in parts:
		message = {}
		for key, value in part.items():
			message[key] = value
		messages.insert_one(message)
	return 'Tested adding python subjects as names for messages'

class Query(graphene.ObjectType):
	messages = graphene.List(MessagesSchema, arg=MessagesInput(required=False))
	def resolve_messages(self, info, arg={}):
		messageInfo = messages.find(arg)
		return list(map(lambda x:
			MessagesSchema(
				id= x['_id'],
				subject= x['subject'],
				html= x['html'],
				fromEmail = x['fromEmail'],
				from_ = x['from'],
				dateTime = x['dateTime']
			),
			list(messageInfo)
		))

class MutateMessage(graphene.Mutation):

	class Arguments:
		arguments = MessagesInput(required=True)

	Output = MessagesSchema

	def mutate(self, info, arguments):
		newMessage = {
			"subject": arguments['subject']
		}
		db.messages.insert_one(newMessage)
		return MessagesInput(
			subject= arguments['subject']
		)

class MyMutation(graphene.ObjectType):
	MutateMessage = MutateMessage.Field()

schema = graphene.Schema(
	query=Query,
	mutation=MyMutation
)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
