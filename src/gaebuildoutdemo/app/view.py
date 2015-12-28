

from pyramid.view import view_config

from pyramid.response import Response


@view_config(route_name='hello')
def welcome_view(request):
    return Response('Hi :) This is a test pyramid application!')

