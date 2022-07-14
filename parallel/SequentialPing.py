from util import FileUtil, PingUtil

def checkAllIpsSequentially(fileName):
    ips = FileUtil.readIPsFromFile(fileName)
    for ip in ips:
        pingIP(ip)


def pingIP(ip):
    flag = PingUtil.isIPReachable(ip);
    if flag:
        formattedOut = "{}: pingable".format(ip)
    else:
        formattedOut = "{}: not pingable".format(ip)
        
    print(formattedOut)
