

from google.appengine.ext.db import Model, IntegerProperty, StringProperty

class Population(Model):
    country = StringProperty()
    count = IntegerProperty()

