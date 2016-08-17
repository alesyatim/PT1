import re
import sys

if len(sys.argv)>1:
    s = sys.argv[1]
else:
    s = 'kklllk khhg jk  ((***))  !! ^^&&^^   dd!!!!!!!$$hhjjl !!'# test string

lst=[]
for i in s.split():
    if len(i)<2:
        lst.append(i)
        continue

    if i[0].isalpha() and i[-1].isalpha():
        lst.append(i)
    else:
        pattern = re.compile('([^0-9a-zA-Z])\\1+')
        new_s = pattern.sub('\\1', i)
        lst.append(new_s)

new_s = ' '.join(lst)
print(new_s)

if len(sys.argv)>1:
    sys.argv[1] = new_s
    print(sys.argv)


# find words (letter starts and end
# f = re.compile('\\b[a-z]\\S*[a-z]\\b')
# res = f.findall(s)
# print(res)

