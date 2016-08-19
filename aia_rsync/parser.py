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
    pattern = re.compile('pass=([a-zA-Z0-9]+)')
    password = pattern.findall(in_str)[0]
    add_password(password)

    # add source and destination
    #pattern = re.compile('')


    return err.errors['Ok']

def add_keys(in_keys):
    keys[:] = in_keys[:]

def add_password(password):
    arguments['password'] = password

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

    test_str = '-v -as -progress -e ssh -i -P pass=HgtG4Fg /dir'
    parse_keys(test_str)
    parse_args(test_str)
    print(keys, arguments)

