from getstats import GetStats
import unittest
import os


class Test_gettests(unittest.TestCase):
	def test_case1(self):		
		obj = GetStats.getstats(dur='10')
		file = obj.run_stats()
		self.assertTrue(os.path.exists(file))


if __name__ == '__main__':
	unittest.main()