

from pyramid.view import view_config

from pyramid.response import Response

from .model import Population


def welcome_view(request):
    population_info = []
    for pop in Population.all().fetch(100):
        population_info.append({'country': pop.country, 'count': pop.count})
    return {'project': 'adamandpaul.gwebdemo', 'populations': population_info}
