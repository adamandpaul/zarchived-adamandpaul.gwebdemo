import unittest

from pyramid import testing

from google.appengine.datastore import datastore_stub_util
from google.appengine.ext import ndb, testbed


class ExampleTests(unittest.TestCase):
    def setUp(self):

        self.config = testing.setUp()

        # Initialize GAE TestBed with datastore
        # see https://cloud.google.com/appengine/docs/python/tools/localunittesting?hl=en
        testbed = testbed.TestBed()
        testbed.activate()
        testbed.init_datastore_v3_stub()
        nbd.get_context().clear_cache()
        self.testbed = testbed

    def tearDown(self):
    	self.testbed.deactivate()
        testing.tearDown()

    def test_welcome_view(self):
        from .view import welcome_view
        request = testing.DummyRequest()
        info = welcome_view(request)
        self.assertEqual(info['project'], 'adamandpaul.gwebdemo')
        self.assertTrue(len(info['populations']))

