import re
import errors as err

separators = [',', '.', ':']  # valid separators between user and name

# path can contain : or not
def check_path(path):
    # check is it file or dir or path
    pass

def check_full_path(path):
    pass

def check_dir(path):
    pattern = re.compile('(/[a-zA-Z0-9_]+)+')
    if pattern.match(path):
        return err.errors['Ok']
    else: return err.errors['NotDir']

def check_file(path):
    pattern = re.compile('([a-zA-Z0-9_]+\.[a-zA-Z0-9_]+)')
    if pattern.match(path):
        return err.errors['Ok']
    else:
        return err.errors['NotFile']

def create_path(path):
    pass

def is_path_exits(path):
    pass

def create_path(path):
    pass

if __name__ == '__main__':
    path1 = '/tmp/dir'
    path2 = 'file.txt'
    path3 = 'user:22@hostname:file.txt'

    err1 = check_dir(path1)
    err2 = check_file(path2)
    print(err1, err2)
