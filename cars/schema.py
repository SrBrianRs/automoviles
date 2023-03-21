import graphene
from graphene_django import DjangoObjectType

from .models import Car


class CarType(DjangoObjectType):
    class Meta:
        model = Car


class Query(graphene.ObjectType):
    cars = graphene.List(CarType)

    def resolve_cars(self, info, **kwargs):
        return Car.objects.all()
    
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
        car=Car(brand=brand,
                model=model,
                color=color,
                version=version,
                year=year,
                engine=engine,
                consumption=consumption,
                price=price,
                airbags=airbags,
                absbreak=absbreak)
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
        )

#4
class Mutation(graphene.ObjectType):
    create_car = CreateCar.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)