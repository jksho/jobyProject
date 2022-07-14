from multiprocessing import Pool

from util import FileUtil, PingUtil

NO_OF_PROCESS = 200

def getIPPingStatus(ip):
    flag = PingUtil.isIPReachable(ip)
    
    if flag:
        formattedOut = "{}: pingable".format(ip)
    else:
        formattedOut = "{}: not pingable".format(ip)
        
    return formattedOut

def checkAllIpsByMultiprocessing(fileName):
    ips = FileUtil.readIPsFromFile(fileName)
    pool = Pool(processes=NO_OF_PROCESS)
    result = pool.map_async(getIPPingStatus, ips)
    pool.close()
    dataList = result.get()
    for i in dataList:
        print(i)