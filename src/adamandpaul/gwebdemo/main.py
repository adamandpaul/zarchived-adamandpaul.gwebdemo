"""Main entry point for this Pyramid App"""


import os
import pkg_resources
import unicodecsv as csv
from .model import Population
from pyramid.config import Configurator


def load_countries():
    """Load country data"""

    # because we are using eggs, we can use pkg_resources to read our data file
    with pkg_resources.resource_stream('adamandpaul.gwebdemo', 'country_data.csv') as data:
        data.readline() # discard header row
        for country, country_local, population in csv.reader(data):
            pop = Population(
                    country=country,
                    country_local=country_local,
                    count=int(population)
                )
            pop.put()


def app_factory(global_config, **settings):
    """Create a Pyramid Application from the config/settings"""


    config = Configurator(settings=settings)

    config.include('pyramid_chameleon')
    config.include('pyramid_zcml')

    config.load_zcml('configure.zcml')

    # initialize the database if it is not there (not sure how safe this is to have here)
    populations = Population.all().fetch(1)
    if len(populations) == 0:
        load_countries()

    return config.make_wsgi_app()
