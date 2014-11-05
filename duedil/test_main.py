# -*- coding: utf-8 -*-
#
#  DuedilApiClient v3 Pro
#  @copyright 2014 Christian Ledermann
#
#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.
#

import unittest

from .v3pro import Client, Company #, Director

from .v3pro import COMPANY_TERM_FILTERS, COMPANY_RANGE_FILTERS


class ClientTestCase(unittest.TestCase):

    def test_url(self):
        client = Client('abcdef')
        self.assertEqual(client.url, 'http://duedil.io/v3')
        client = Client('abcdef', True)
        self.assertEqual(client.url, 'http://duedil.io/v3/sandbox')
        client = Client('abcdef', False)
        self.assertEqual(client.url, 'http://duedil.io/v3')

    def test_key(self):
        client = Client('abcdef')
        self.assertEqual(client.api_key, 'abcdef')


class SearchCompaniesTestCase(unittest.TestCase):

    client = Client('x425dum7jp2jxuz7e3ktaqmx', True)

    def test_kwargs(self):
        # you have to search for something
        with self.assertRaises(AssertionError):
            self.client.search_company()
         # search terms are strings
        with self.assertRaises(AssertionError):
            self.client.search_company(bla=2)
        # search ranges have a upper and lower
        # numerical value
        with self.assertRaises(AssertionError):
            self.client.search_company(name=1)
        with self.assertRaises(AssertionError):
            self.client.search_company(employee_count=1)
        with self.assertRaises(AssertionError):
            self.client.search_company(employee_count=[1,2,3])
        with self.assertRaises(AssertionError):
            self.client.search_company(employee_count=[2,'100'])
        # and this one must pass:
        self.client.search_company(name='ex')

    def test_order_by(self):
        with self.assertRaises(AssertionError):
            self.client.search_company(name='ex', order_by='None')
        self.client.search_company(order_by={'field': 'employee_count', 'direction':'asc'},
            name='ex')

    def test_limit(self):
        with self.assertRaises(AssertionError):
            self.client.search_company(name='ex', limit='0')
        self.client.search_company(name='ex', limit=1)

    def test_offset(self):
        with self.assertRaises(AssertionError):
            self.client.search_company(name='ex', offset='0')
        self.client.search_company(name='ex', offset=0)

class SearchDirectorsTestCase(unittest.TestCase):

    client = Client('x425dum7jp2jxuz7e3ktaqmx', True)



class CompanyTestCase(unittest.TestCase):

    pass

class DirectorTestCase(unittest.TestCase):

    pass


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ClientTestCase))
    suite.addTest(unittest.makeSuite(SearchCompaniesTestCase))
    suite.addTest(unittest.makeSuite(SearchDirectorsTestCase))
    suite.addTest(unittest.makeSuite(CompanyTestCase))
    suite.addTest(unittest.makeSuite(DirectorTestCase))
    return suite

if __name__ == '__main__':
    unittest.main()
