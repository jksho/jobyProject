import unittest
from util import FileUtil, PingUtil

class TestpingIP(unittest.TestCase):
    def test_ping(self):
        """
        Test that it can ping 172.16.1.1 (gateway)
        """
        test_ipAddress = "172.16.1.1"
        result = PingUtil.isIPReachable(test_ipAddress);
        self.assertEqual(result,True)
        
if __name__ == '__main__':
    unittest.main()