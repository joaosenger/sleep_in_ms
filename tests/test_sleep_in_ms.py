from src.sleep_in_ms.sleep import sleep_in_ms
import time
import unittest

'''
Example of usage:

python3 -m unittest discover tests
'''


class TestSleepInMs(unittest.TestCase):

    def test_sleep_success(self):
        start_time = time.time()
        duration_ms = 500
        result = sleep_in_ms(duration_ms)
        end_time = time.time()

        elapsed_ms = (end_time - start_time) * 1000

        self.assertTrue(result)
        self.assertAlmostEqual(elapsed_ms, duration_ms, delta=50)

    def test_invalid_type(self):
        self.assertFalse(sleep_in_ms("1000"))
        self.assertFalse(sleep_in_ms(None))

    def test_zero_time(self):
        self.assertTrue(sleep_in_ms(0))


if __name__ == '__main__':
    unittest.main()
