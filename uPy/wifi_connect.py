# ---------------------------------------
#  _____  __  __ _______        __   ___  
# |  __ \|  \/  |__   __|      /_ | / _ \ 
# | |__) | \  / |  | |    __   _| || | | |
# |  ___/| |\/| |  | |    \ \ / / || | | |
# | |    | |  | |  | |     \ V /| || |_| |
# |_|    |_|  |_|  |_|      \_/ |_(_)___/ 
# ----------------------------------------
#  Version 1.0
#  microPython Firmware esp32spiram-idf3-20191220-v1.12
#  Filename : wifi_connect.py

from network import WLAN
from post import *
from usocket import getaddrinfo, socket, AF_INET, SOCK_STREAM
from utime import sleep

def station_connected(station: WLAN) -> bool:
    print("Connected...Testing Access...")
    target_host = "www.google.com"
    target_port = 80
    sock = socket(AF_INET,SOCK_STREAM)
    # time in seconds
    sock.settimeout(0.5)
    # address resolving
    sockaddr = getaddrinfo(target_host, target_port)
    print (str(sockaddr))
    # send some data 
    request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host
    try:
        sock.connect(sockaddr[0][-1])
        sock.send(request.encode()) 
        # receive some data 
        response = sock.recv(4096)  
        http_response = repr(response)
        http_response_len = len(http_response)
        print(str(http_response[0:14]))
        print("Internet Accessible")
        response = post_data(url, headers, ','.join(dataCSV))
        if response.status_code == 200:
            print("Post Request Successful")
            return True
    except OSError as e:
        print(e)
        print("Internet Not Accessible")
        
