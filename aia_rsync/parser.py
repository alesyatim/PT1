import re
import errors as err

arguments = {
    'source':'',
    'destination':'',
    'password':''
}
keys = []

def parse_data(in_str):
     pass

def parse_keys(in_str):
    pattern = re.compile('(-[a-z ]+) ')
    res = pattern.findall(in_str)
    add_keys(res)
    return err.errors['Ok']

def parse_args(in_str):
    pass

def add_keys(in_keys):
    keys[:] = in_keys[:]

def add_arguments(**kwargs):
    pass

def get_source():
    source = ''
    return source

def get_dest():
    dest = ''
    return dest

def get_keys():
    pass

def get_arguments():
    pass

if __name__ == '__main__':

    test_str = '-v -as -progress -e ssh -i -P /dir'
    parse_keys(test_str)
    print(keys)

