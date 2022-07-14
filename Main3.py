from timeit import default_timer as timer

from createIPList.createDefault import generateIPList
from parallel.SequentialPing import checkAllIpsSequentially
from parallel.MultiThreadingPing import checkAllIpsByMultiThreading
from parallel.MulitprocessingPing import checkAllIpsByMultiprocessing

FILE_NAME = "IPList/ipaddress-generated.txt"
ip_addr_range_1 = "171.16.1"    # Default values for subnet #1
ip_addr_range_2 = "171.16.2"    # Default values for subnet #2
excluded_octet = "1"            # Default value for octet to exclude

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
    # print("Sequential Results")
    # executeSequentiall()
    # print("Multiprocessing Results")
    # executeMultiprocessing()
    print("Multithreading Results:")
    executeMultiThreaded() # 10.679292550019454  seconds
    end = timer()
    result = end - start
    print("Total Time Taken: ", result, " seconds")
