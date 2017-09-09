import unittest
import _util

from Core.input import *

class TestStringInput(unittest.TestCase):

    def test_nullString_returnsZero(self):
        o = StringInput('')
        for i in range(10):
            with self.subTest(i=i):
                self.assertEqual(o.getNext(), 0)

    def test_arbString_returnsSame(self):
        s = 'tesing string'
        o = StringInput(s)
        for i in range(len(s)):
            with self.subTest(i=i):
                self.assertEqual(o.getNext(), ord(s[i]))

    def test_arbString_zeroAfterString(self):
        s = 'arbitrary string'
        o = StringInput(s)
        for i in range(len(s)):
            with self.subTest(i=i):
                self.assertEqual(o.getNext(), ord(s[i]))
        for i in range(10):
            with self.subTest(i=i):
                self.assertEqual(o.getNext(), 0)

#TODO: test StdinInput ?