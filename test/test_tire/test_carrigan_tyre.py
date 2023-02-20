import unittest

from tyre.carrigan_tyre import CarriganTyre

class TestCarrigan(unittest.TestCase):
    def test_tyre_should_be_serviced(self):
        array = [1,0.3,0.9,0.5]
        tyre = CarriganTyre(array)
        self.assertTrue(tyre.needs_service())

    def test_tyre_should_not_be_serviced(self):
        array = [0.3, 0.8, 0.4, 0.5]
        tyre = CarriganTyre(array)
        self.assertFalse(tyre.needs_service())