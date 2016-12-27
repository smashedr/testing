from django.test import TestCase
from django.core.urlresolvers import reverse


class TestViews(TestCase):
    def setUp(self):
        self.views = ['home', 'django', 'python']

    def test_views(self):
        for view in self.views:
            print('Testing reverse for view: %s' % view)
            response = self.client.get(reverse(view))
            self.assertEqual(response.status_code, 200)
