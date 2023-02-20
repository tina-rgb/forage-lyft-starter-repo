import unittest

from tyre.octoprime_tyre import OctoprimeTyre

class TestOctoprime(unittest.TestCase):
    def test_tyre_should_be_serviced(self):
        array = [3, 4, 2, 1]
        tyre = OctoprimeTyre(array)
        self.assertTrue(tyre.needs_service())

    def test_tyre_should_not_be_serviced(self):
        array = [1, 2, 2.5, 2]
        tyre = OctoprimeTyre(array)
        self.assertFalse(tyre.needs_service())