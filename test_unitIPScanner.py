import unittest
from util import FileUtil, PingUtil

class TestpingIP(unittest.TestCase):
    def test_ping(self):
        """
        Test that it can ping 127.0.0.1 (gateway)
        """
        test_ipAddress = "127.0.0.1"
        result = PingUtil.isIPReachable(test_ipAddress);
        self.assertEqual(result,True)
        
if __name__ == '__main__':
    unittest.main()