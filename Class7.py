import re

def parse_devices(lst):
    pattern1=re.compile('sd[a-z]{1,2}[0-9]{1,2}')
    pattern2=re.compile('sd[a-z]{1,2}$')
    part = [dev for dev in lst if pattern1.search(dev)]
    block = [dev for dev in lst if pattern2.search(dev)]
    print('====', part, block)

    P = set(part)
    X = set([dev[:-1] for dev in part])
    B = set(block).difference(X)
    devices = dict()
    devices['block']=list(B)
    devices['part']=part
    print(devices)
    return devices

lst = ['sda', 'sdb', 'sdb1', 'sdb2', 'sdb3','sdb99', 'sdc', 'sdc3']
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