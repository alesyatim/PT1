import re
arguments = {
    'source':'',
    'destination':'',
    'password':''
}
keys = []

def parse_data(in_str):
    try:
        pattern = re.compile('(-[a-z ]+) ')
        res = pattern.findall(in_str)
        keys = res
        print(res)
    except:
        pass

if __name__ == '__main__':

    test_str = '-v -as -progress -e ssh -i -P /dir'

    parse_data(test_str)