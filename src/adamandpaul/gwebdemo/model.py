

from google.appengine.ext.db import Model, IntegerProperty, StringProperty

class Population(Model):
    country = StringProperty()
    country_local = StringProperty()
    count = IntegerProperty()

