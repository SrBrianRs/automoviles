import graphene
from graphene_django import DjangoObjectType
from users.schema import UserType
from graphql import GraphQLError
from django.db.models import Q
from .models import Consulta
from consultas.models import Consulta

class ConsultaType(DjangoObjectType):
    class Meta:
        model = Consulta  


class Query(graphene.ObjectType):
    consultas = graphene.List(ConsultaType, search=graphene.String())

    def resolve_consultas(self, info, search=None, **kwargs):
        # The value sent with the search parameter will be in the args variable
        if search:
            filter = (
                Q(result__icontains=search) |
                Q(modelo__icontains=search) |
                Q(prompt__icontains=search) 
            )
            return Consulta.objects.filter(filter)

        return Consulta.objects.all()
    
#2
class CreateConsulta(graphene.Mutation):
    id  = graphene.Int()
    fecha = graphene.String()
    modelo = graphene.String()
    prompt = graphene.String()
    result = graphene.String()
    
    
    posted_by = graphene.Field(UserType)
    
    class Arguments:
        fecha = graphene.String()
        modelo = graphene.String()
        prompt = graphene.String()
        result = graphene.String()
        
        
            


#3
    def mutate(self, info, result, modelo, fecha, prompt):
        user = info.context.user or None

        consulta=Consulta(
                fecha=fecha,
                modelo=modelo,
                prompt=prompt,
                result=result,
                posted_by=user,
                )
        consulta.save()

        return CreateConsulta(
            id = consulta.id,
            fecha=consulta.fecha,
            modelo=consulta.modelo,
            prompt=consulta.prompt,
            result=consulta.result,
            posted_by=consulta.posted_by,
        )

#4

class Mutation(graphene.ObjectType):
    create_consulta = CreateConsulta.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)