#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from stringcalculator import StringCalculator

class StringCalculatorTest (unittest.TestCase):
    def test_empty_string(self):
        sut = StringCalculator()
        self.assertEqual(0, sut.add(""))

if __name__ == '__main__':
    unittest.main()