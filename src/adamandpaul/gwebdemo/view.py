

from pyramid.view import view_config

from pyramid.response import Response

from .model import Population

from num2words import num2words

def welcome_view(request):
    population_info = []
    for pop in Population.all().fetch(100):
        population_info.append({'country': pop.country, 'count': num2words(pop.count).title()})
    return {'project': 'adamandpaul.gwebdemo', 'populations': population_info}
