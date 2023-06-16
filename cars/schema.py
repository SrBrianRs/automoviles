import graphene
from graphene_django import DjangoObjectType
from users.schema import UserType
from .models import Car
from cars.models import Car, Vote
from graphql import GraphQLError
from django.db.models import Q







class CarType(DjangoObjectType):
    class Meta:
        model = Car
class VoteType(DjangoObjectType):
    class Meta:
        model = Vote   


class Query(graphene.ObjectType):
    cars = graphene.List(CarType, search=graphene.String())
    votes = graphene.List(VoteType)

    def resolve_cars(self, info, search=None, **kwargs):
        # The value sent with the search parameter will be in the args variable
        if search:
            filter = (
                Q(brand__icontains=search) |
                Q(model__icontains=search)
            )
            return Car.objects.filter(filter)

        return Car.objects.all()

    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()
    
#2
class CreateCar(graphene.Mutation):
    id  = graphene.Int()
    brand = graphene.String()
    model = graphene.String()
    color = graphene.String()
    version = graphene.String()
    year = graphene.Int()
    engine = graphene.String()
    consumption = graphene.Decimal()
    price = graphene.Decimal()
    airbags = graphene.Boolean()
    absbreak = graphene.Boolean()
    posted_by = graphene.Field(UserType)

    
    class Arguments:
            brand = graphene.String()
            model = graphene.String()
            color = graphene.String()
            version = graphene.String()
            year = graphene.Int()
            engine = graphene.String()
            consumption = graphene.Decimal()
            price = graphene.Decimal()
            airbags = graphene.Boolean()
            absbreak = graphene.Boolean()
            


#3
    def mutate(self, info, brand, model, color, version, year, engine, consumption, price, airbags, absbreak):
        user = info.context.user or None

        car=Car(brand=brand,
                model=model,
                color=color,
                version=version,
                year=year,
                engine=engine,
                consumption=consumption,
                price=price,
                airbags=airbags,
                absbreak=absbreak,
                posted_by=user,
                

                )
        car.save()

        return CreateCar(
            id = car.id,
            brand=car.brand,
            model=car.model,
            color=car.color,
            version=car.version,
            year=car.year,
            engine=car.engine,
            consumption=car.consumption,
            price=car.price,
            airbags=car.airbags,
            absbreak=car.absbreak,
            posted_by=car.posted_by,
        )

#4




class CreateVote(graphene.Mutation):
    user = graphene.Field(UserType)
    car = graphene.Field(CarType)

    class Arguments:
        car_id = graphene.Int()

    def mutate(self, info, car_id):
        user = info.context.user
        if user.is_anonymous:
             #1
            raise GraphQLError('You must be logged to vote!')


        car = Car.objects.filter(id=car_id).first()
        if not car:
           #2
            raise Exception('Invalid Link!')
            

        Vote.objects.create(
            user=user,
            car=car,
        )

        return CreateVote(user=user, car=car)

class Mutation(graphene.ObjectType):
    create_car = CreateCar.Field()
    create_vote = CreateVote.Field()





schema = graphene.Schema(query=Query, mutation=Mutation)