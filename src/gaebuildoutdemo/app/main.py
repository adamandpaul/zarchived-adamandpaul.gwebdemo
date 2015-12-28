


from pyramid.config import Configurator


def app_factory(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('hello', '/')
    config.scan()
    return config.make_wsgi_app()
