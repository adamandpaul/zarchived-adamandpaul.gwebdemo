
from gaebuildoutdemo.app.view import welcome_view

from pyramid.config import Configurator


def app_factory(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('hello', '/hello')
    config.add_view(welcome_view, 'hello')
    return config.make_wsgi_app()
