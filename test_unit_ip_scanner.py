import unittest
#import ping3
import util import FileUtil, PingUtil

def test_ping(self):
    test_ipAddress = "172.16.1.1"
     flag = PingUtil.isIPReachable(ip);
    if flag:
        formattedOut = "{}: pingable".format(ip)
    else:
        formattedOut = "{}: not pingable".format(ip)
    return(formattedOut)
    # ping3.EXCEPTIONS = True
    # try:
    #     ping3.ping(test_ipAddress)
    # except ping3.errors.HostUnknown:  # Specific error is catched.
    #     print("Host unknown error raised.")
    # except ping3.errors.PingError:  # All ping3 errors are subclasses of `PingError`.
    #     print("A ping error raised.")