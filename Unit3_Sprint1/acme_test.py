#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
    #stealability()
    def test_default_stealability(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertTrue(prod.stealability, 'Not so stealable...')
    #explode()
    def test_default_explode(self):
        prod = Product('Test Product')
        self.assertFalse(prod.explode, '...fizzle')
class AcmeReportTests(unittest.TestCase):
    #checks that it really does receive a list of length 30
    def test_default_num_products(self):
        self.
    #assertIn - checks that the generated names for a default batch of 
    #products are all valid possible names to generate 
    #(adjective, space, noun, from the lists of possible words)
    def test_legal_names(self):
        self.assertIn()


if __name__ == '__main__':
    unittest.main()