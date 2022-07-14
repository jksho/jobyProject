import unittest
import ping3
from util import FileUtil, PingUtil
from parallel.SequentialPing import checkAllIpsSequentially
from parallel.MultiThreadingPing import checkAllIpsByMultiThreading
from parallel.MulitprocessingPing import checkAllIpsByMultiprocessing

def test_ping(self):
    test_ipAddress = "172.16.1.1"
    ping3.EXCEPTIONS = True
    try:
        ping3.ping("not.exist.com")
    except ping3.errors.HostUnknown:  # Specific error is catched.
        print("Host unknown error raised.")
    except ping3.errors.PingError:  # All ping3 errors are subclasses of `PingError`.
        print("A ping error raised.")