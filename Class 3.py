L = 'Namespaces are one honking great idea -- let\'s do more of those!'
d = {}
for letter in  set(L):
      d[letter] = L.count(letter)

keys = sorted(d, key=lambda x: d[x])
for key in keys:
    print('{}={}'.format(key,d[key]))



