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