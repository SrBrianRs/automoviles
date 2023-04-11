from django.test import TestCase

# Create your tests here.

from graphene_django.utils.testing import GraphQLTestCase
from mixer.backend.django import mixer
import graphene
import json


from cars.schema import schema
from cars.models import Car

CARS_QUERY = '''
 {
   cars {
     id
     brand
     model
     color
     version
     year
     engine
     consumption
     price
     airbags
     absbreak
   }
 }
'''

CREATE_CAR_MUTATION = '''
 mutation createCarMutation($absbreak: Boolean,$airbags: Boolean,$brand: String,$color: String, $consumption: Decimal, $engine: String, $model: String, $price: Decimal, $version: String, $year: Int) {    
    createCar(absbreak: $absbreak, airbags: $airbags, brand: $brand, color: $color, consumption: $consumption, engine: $engine, model: $model, price: $price, version: $version,year: $year) {  
    model
    }
 }
'''


class CarTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    def setUp(self):
        self.car1 = mixer.blend(Car)
        self.car2 = mixer.blend(Car)

    def test_cars_query(self):
        response = self.query(
            CARS_QUERY,
        )
        content = json.loads(response.content)
        # print(content)
        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)
        print("query cars results ")
        print(content)
        assert len(content['data']['cars']) == 2



    def test_createCar_mutation(self):

            response = self.query(
                CREATE_CAR_MUTATION,
                variables={'absbreak': True,'airbags': 6,'brand': 'Chevrolet','color': 'Red','consumption': 10.5,'engine': '1.0L','model': 'Onix','price': 15000,'version': 'LT','year': 2022}

            )
            print('mutation')
            print(response)
            content = json.loads(response.content)
            print(content)
            self.assertResponseNoErrors(response)
            self.assertDictEqual({"createCar": {"model": "Onix"}}, content['data']) 

