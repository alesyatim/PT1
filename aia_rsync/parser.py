import re
import errors as err

arguments = {
    'source':'',
    'destination':'',
    'password':''
}
keys = []
availible_single_keys = ['P', 'a', 'v', 'S', 'z', 'q', 'i']
availible_complicated_keys = ['progress', 'e ssh']

def parse_data(in_str):
     pass

def parse_keys(in_str):
    pattern = re.compile('-([a-z ]+) ')
    res = pattern.findall(in_str)
    add_keys(res)
    return err.errors['Ok']

# def split_keys():
#     tmp = [list(key) for key in keys if not check_complicated_keys(key)]
#     print(tmp)

def check_single_keys(key):
    if key in availible_single_keys:
        return True

def check_complicated_keys(key):
    if key in availible_complicated_keys:
        return True

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
    
def parse_machine(input_string):
    parse_in_str = re.split(r'[:,@]', input_string)
    user_name = parse_in_str[:1]
          #validation user_name
    port_name = parse_in_str[1:2]
          #validation port_name
    ip_adr = parse_in_str[2:3]
          #validation ip_adr
    name_of_file = parse_in_str[3:4]
          #validation name_of_file
    return user_name, port_name, ip_adr, name_of_file

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
    split_keys()
    #print(keys)

