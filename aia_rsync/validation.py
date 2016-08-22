# -*- coding: utf-8 -*-
import re
import socket
import errors as err

separators = [',', '.', ':']  # valid separators between user and name

# path can contain : or not
def check_path(path):
    # check is it file or dir or path
    pass

def check_full_path(path):
    pattern = re.compile('([a-zA-Z]+[,:\.][0-9]{0,4}@([a-zA-z]+|[0-9\.]+):[a-zA-Z0-9_]+\.[a-zA-Z0-9]+)')
    res =  pattern.match(path)
    print(res.groups())
    if res:
        return err.errors['Ok']
    else:
        return err.errors['NotPath']

def check_dir(path):
    pattern = re.compile('(/[a-zA-Z0-9_]+)+')
    res = pattern.match(path)
    print(res.groups())
    if res:
        return err.errors['Ok']
    else: return err.errors['NotDir']

def check_file(path):
    pattern = re.compile('([a-zA-Z0-9_]+\.[a-zA-Z0-9_]+)')
    res = pattern.match(path)
    print(res.groups())
    if res:
        return err.errors['Ok']
    else:
        return err.errors['NotFile']

def create_path(path):  # create Dir's if path isn't exist
    if is_path_exits(path) != 0:
        os.makedirs(path)
        return err.errors['PathCreated']
    else:
        return err.errors['OK']
    pass


def is_path_exits(path):
    if os.path.exists(path):
        return err.errors['Ok']
    else:
        return err.errors['PathNotFound']
    pass



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
            
#___scan_port____#
from socket import *

def scan_free_port(targetIP):
        print 'Starting scan on host...', targetIP
        for i in xrange(0, 65535):
            s = socket(AF_INET, SOCK_STREAM)
            result = s.connect_ex((targetIP, i))
            if(result == 0) :
                list_of_free_ports = i
                print('Port {} OPEN'.format(list_of_free_ports,))
            s.close()
        print (list_of_free_ports)

if __name__ == '__main__':
    path1 = '/tmp/dir'
    path2 = 'file.txt'
    path3 = 'user:22@hostname:file.txt'

    err1 = check_dir(path1)
    err2 = check_file(path2)
    err3 = check_full_path(path3)
    print(err1, err2, err3)

scan_free_port('127.0.0.1')
