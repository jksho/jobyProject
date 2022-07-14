    
    def 
    'ip_addr_range_1 = input ('first ip range to scan x.y.z first 3 octet (ie. 172.16.1)\n')
    if not ip_addr_range_1:
        ip_addr_range_1 = "171.16.1"    # Default values for subnet #1
    ip_addr_range_2 = input ('second ip range to scan x.y.z first 3 octet (ie. 172.16.2)\n')
    if not ip_addr_range_2:
        ip_addr_range_2 = "171.16.2"    # Default values for subnet #1
    excluded_octet = input('What last octet do you want to exclude in the scan? 1 to 254\n')
    if not excluded_octet:
        excluded_octet = "1"    # Default values for final octet
    ignore = [0,int(excluded_octet)]
    print ("excluding " + ip_addr_range_1 + "." + excluded_octet)
    print ("excluding " + ip_addr_range_2 + "." + excluded_octet)
    scan_list = [ind for ind in range(255) if ind not in ignore]
    ip_scan_file = open(FILE_NAME, 'w+')
    for ip_last_octet in scan_list:
        ip_scan_file.write("{}.{}\n".format(ip_addr_range_1, ip_last_octet))
        ip_scan_file.write("{}.{}\n".format(ip_addr_range_2, ip_last_octet))
    ip_scan_file.close()  # Close the created file