import re
# path can contain : or not

def check_path(in_str):
    try:
        pass
    except:
        pass

# ______ip validation________
import socket

def is_ip (s_string):
    try:
        socket.inet_pton (socket.AF_INET6, s_string) #Convert an IP address from string format to a packed string suitable
                                                     #for use with low-level network functions.
                                                     # AF_INET for IPv4, AF_INET6 for IPv6  ()
                                                     # AF_INET, AF_UNIX -- socket domains (first argument to socket() call)
        return True
    except socket.error:
        try:
            socket.inet_pton (socket.AF_INET, s_string)
            return True
        except:
            return False

#s_string='fe80:0:0:0:200:f8ff:fe21:67cf'
#print(s_string)
#z=is_ip(s_string)
#print(z)
