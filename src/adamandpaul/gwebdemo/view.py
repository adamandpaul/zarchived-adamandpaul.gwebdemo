"""Module containing the application views"""

from .model import Population
from pyramid.response import Response
from pyramid.view import view_config


def welcome_view(request):
    """Pyramid view returning a list of countries stored
    in the model and their populations. Sorted by most
    hightest population first
    """
    population_info = []
    for pop in Population.all().order('-count').fetch(100):
        info = {}
        info['country'] = pop.country
        info['country_local'] = pop.country_local
        info['count'] = pop.count
        population_info.append(info)
    return {'populations': population_info}
