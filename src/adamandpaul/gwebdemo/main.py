
import os

from pyramid.config import Configurator


from .model import Population


def load_countries():
    country_data = [
      ('China', 1374000000),
      ('India', 1282210000),
      ('USA', 322532000),
      ('Indonesia', 255461700),
      ('Brazil', 205406000 ),
    ]

    for country, population in country_data:
        pop = Population(country=country, count=population)
        pop.put()


def app_factory(global_config, **settings):

    is_dev = os.environ.get("SERVER_SOFTWARE", 'Dev').startswith("Dev")

    config = Configurator(settings=settings)

    if is_dev:
        #config.include('pyramid_debugtoolbar')

        # Google App Engine doesn't allow this.
        # so we will just overrride it so debug tool bar
        # can do it's introspections
        import platform
        platform.platform = lambda: 'blah'

    config.include('pyramid_chameleon')
    config.include('pyramid_zcml')

    config.load_zcml('configure.zcml')

    # initialize the database if it is not there (not sure how safe this is to have here)
    populations = Population.all().fetch(1)
    if len(populations) == 0:
        load_countries()

    return config.make_wsgi_app()
