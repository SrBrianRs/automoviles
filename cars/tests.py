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
        #print(content)
        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)
        print ("query cars results ")
        print (content)
        assert len(content['data']['cars']) == 2
