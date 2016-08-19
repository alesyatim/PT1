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

def create_path(path):
    pass

def is_path_exits(path):
    pass

def create_path(path):
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

if __name__ == '__main__':
    path1 = '/tmp/dir'
    path2 = 'file.txt'
    path3 = 'user:22@hostname:file.txt'

    err1 = check_dir(path1)
    err2 = check_file(path2)
    err3 = check_full_path(path3)
    print(err1, err2, err3)
