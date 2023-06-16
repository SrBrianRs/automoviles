import graphene

import cars.schema
import consultas.schema
import users.schema
import graphene
import graphql_jwt

class Query(consultas.schema.Query, users.schema.Query,cars.schema.Query, graphene.ObjectType):
    pass

class Mutation(consultas.schema.Mutation, users.schema.Mutation,  cars.schema.Mutation, graphene.ObjectType):
    
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    


schema = graphene.Schema(query=Query, mutation=Mutation)
