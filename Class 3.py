L = 'Namespaces are one honking great idea -- let\'s do more of those!'
d = {}
for letter in  set(L):
      d[letter] = L.count(letter)

for k, v in d.items():
    print('{}={}'.format(k,v))



