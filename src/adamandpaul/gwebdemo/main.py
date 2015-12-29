
import os

from pyramid.config import Configurator


def app_factory(global_config, **settings):

    is_dev = os.environ.get("SERVER_SOFTWARE", 'Dev').startswith("Dev")

    config = Configurator(settings=settings)

    if is_dev:
        config.include('pyramid_debugtoolbar')

        # Google App Engine doesn't allow this.
        # so we will just overrride it so debug tool bar
        # can do it's introspections
        import platform
        platform.platform = lambda: 'blah'

    config.include('pyramid_chameleon')
    config.include('pyramid_zcml')

    config.load_zcml('configure.zcml')





    config.scan()
    return config.make_wsgi_app()
