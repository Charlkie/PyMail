import graphene

# Specifies types of collection
class MessagesSchema(graphene.ObjectType):
	id = graphene.ID()
	subject = graphene.String()
	html = graphene.String()
	fromEmail = graphene.String()
	from_ = graphene.String()
	dateTime = graphene.String()