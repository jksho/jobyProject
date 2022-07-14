from timeit import default_timer as timer

from createIPList.createDefault import generateIPList
from parallel.SequentialPing import checkAllIpsSequentially
from parallel.MultiThreadingPing import checkAllIpsByMultiThreading
from parallel.MulitprocessingPing import checkAllIpsByMultiprocessing

FILE_NAME = "IPList/ipaddress-generated.txt"
# Default values for subnet #1
ip_addr_range_1 = "192.168.1"
# Default values for subnet #2   
ip_addr_range_2 = "192.168.2"
 # Default value for octet to exclude
excluded_octet = "56"          

def createIPList():
    generateIPList(FILE_NAME)

def executeSequentiall():
    checkAllIpsSequentially(FILE_NAME)

def executeMultiThreaded():
    checkAllIpsByMultiThreading(FILE_NAME)

def executeMultiprocessing():
    checkAllIpsByMultiprocessing(FILE_NAME)


if __name__ == '__main__':
    createIPList()
    start = timer()
    # print("Sequential Results:")
    # executeSequentiall() # 7156.473847672 seconds ping 5 counts
    # print("MultiProcessing Results:")
    # executeMultiprocessing() #  47.99978301899998 seconds ping 5 counts
    print("MultiThreading Results:")
    executeMultiThreaded() # 30.525291863000348 seconds ping 5 counts
    end = timer()
    result = end - start
    print("Total Time Taken: ", result, " seconds")
