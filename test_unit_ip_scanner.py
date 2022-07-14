import unittest
from util import FileUtil, PingUtil

def test_ping(self):
    test_ipAddress = "172.16.1.1"
    flag = PingUtil.isIPReachable(test_ipAddress);
    if flag:
        formattedOut = "{}: pingable".format(ip)
    else:
        formattedOut = "{}: not pingable".format(ip)
    return(formattedOut)