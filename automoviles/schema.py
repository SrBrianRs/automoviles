import graphene

import cars.schema


class Query(cars.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)