
import unittest

from .main import load_countries
from pyramid import testing
from google.appengine.datastore import datastore_stub_util
from google.appengine.ext import ndb, testbed


class ExampleTests(unittest.TestCase):
    def setUp(self):

        # Initialize GAE TestBed with datastore
        # see https://cloud.google.com/appengine/docs/python/tools/localunittesting?hl=en
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        ndb.get_context().clear_cache()

        # Initialize Pyramid
        self.config = testing.setUp()
        load_countries()


    def tearDown(self):
        testing.tearDown()
    	self.testbed.deactivate()

    def test_welcome_view(self):
        from .view import welcome_view
        request = testing.DummyRequest()
        info = welcome_view(request)
        self.assertTrue(len(info['populations']) > 0)

