import re

def parse_devices(lst):
    part = []
    for dev in lst:
        pattern = re.compile('sd[a-z]{1,2}[0-9]{1,2}')
        res = pattern.findall(dev)
        if not len(res)==0:
            part.append(res[0])
    print(part)
    P = set(part)
    A = set(lst)
    C = A.difference(P)
    temp=[]
    for dev in part:
        if dev[-2].isdigit():
            temp.append(dev[:-2])
        else: temp.append(dev[:-1])
    X = set(temp)
    print(X)
    B = C.difference(X)
    print(B)

    devices = dict()
    devices['block']=list(B)
    devices['part']=list(part)
    print(devices)
    return devices

lst = ['sda', 'sdb', 'sdb1', 'sdb2', 'sdb3', 'sdc']
parse_devices(lst)

# def parse_date(strg):
#     patern = '([0-9]{4})-([0-9]{1,2})-([0-9]{1,2})T([0-9]{1,2}):([0-9]{1,2}):([0-9]{1,2})\.[0-9]*'
#     p = re.compile(patern)
#     res = p.findall(strg)
#     print(res)
#     t_s = dict()
#     t_s['hour'] = res[0][3]
#     t_s['minute'] = res[0][4]
#     t_s['second'] = res[0][5]
#     d_s = dict()
#     d_s['year'] = res[0][0]
#     d_s['month'] = res[0][1]
#     d_s['day'] = res[0][2]
#     return (t_s, d_s)
#
# time_stamp, date_stamp = parse_date('2014-9-1T12:48:3.')
# print(time_stamp, date_stamp)