import graphene

# Arguments you want to query
class MessagesInput(graphene.InputObjectType):
	_id = graphene.ID(required=False)
	name = graphene.String(required=False)