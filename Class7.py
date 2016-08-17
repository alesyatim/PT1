import re

# def dev(lst):
#     s=''
#     devices = dict()
#     l_block=[]
#     l_part=[]
#     devices['block']=l_block
#     devices['part']=l_part
#     for i in lst:
#         s+=i
#     print(s)
#     for i in lst:
#         p = re.compile(i+'[0-9]{1,2}')
#         res = p.findall(s)
#         print(res)
#         if len(res)==0:
#             devices['block'].append(i)
#         else:
#             temp = res[:]
#             l_part.append(res)
#
#     print(devices)

def dev(lst):
    devices = dict()
    part = []
    for dev in lst:
        p = re.compile('[a-z]{3}[0-9]{1,2}')
        res = p.findall(dev)
        if not len(res)==0:
            part.append(res[0])
            print(res)
    print(part)
    set_part=set(part)
    set_all=set(lst)
    x = set_all.difference(set_part)
    print(x)
    print(set_part, set_all)
    for dev in part:
        p = re.compile(dev[0:2])
        #res =



    l_block=[]
    l_part=[]
    devices['block']=l_block
    devices['part']=l_part
    print(devices)

lst = ['sda', 'sdb', 'sdb1', 'sdb2', 'sdb3', 'sdc']
dev(lst)

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