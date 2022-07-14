from timeit import default_timer as timer

from parallel.SequentialPing import checkAllIpsSequentially
from parallel.MultiThreadingPing import checkAllIpsByMultiThreading
from parallel.MulitprocessingPing import checkAllIpsByMultiprocessing

FILE_NAME = "testData/ipaddress-512.txt"
ip_addr_range_1 = "171.16.1"    # Default values for subnet #1
ip_addr_range_2 = "171.16.2"    # Default values for subnet #2
excluded_octet = "1"            # Default value for octet to exclude

def executeSequentiall():
    checkAllIpsSequentially(FILE_NAME)

def executeMultiThreaded():
    checkAllIpsByMultiThreading(FILE_NAME)

def executeMultiprocessing():
    checkAllIpsByMultiprocessing(FILE_NAME)

if __name__ == '__main__':
    ip_addr_range_1 = input ('first ip range to scan x.y.z first 3 octet (ie. 172.16.1)\n')
    if ip_ddr_range_1
    ip_addr_range_2 = input ('second ip range to scan x.y.z first 3 octet (ie. 172.16.2)\n')
    excluded_octet = input('What last octet do you want to exclude in the scan? 1 to 254\n')
    ignore = [0,int(excluded_octet)]
    print ("excluding " + ip_addr_range_1 + "." + excluded_octet)
    print ("excluding " + ip_addr_range_2 + "." + excluded_octet)
    scan_list = [ind for ind in range(255) if ind not in ignore]
    ip_scan_file = open(FILE_NAME, 'w+')
    for ip_last_octet in scan_list:
        ip_scan_file.write("{}.{}\n".format(ip_addr_range_1, ip_last_octet))
        ip_scan_file.write("{}.{}\n".format(ip_addr_range_2, ip_last_octet))
    ip_scan_file.close()  # Close the created file
    
    start = timer()
    
    # print("Sequential Results")
    # executeSequentiall() # 163.009457  seconds
    # print("Multiprocessing Results")
    # executeMultiprocessing() # 14.33898959698854  seconds
    print("Multithreading Results:")
    executeMultiThreaded() # 10.679292550019454  seconds


    end = timer()
    result = end - start
    print("Total Time Taken: ", result, " seconds")
