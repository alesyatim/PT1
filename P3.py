L = 'The Zen of Python by Tim Peters'

# 1
def to_weird(in_str):
    lst = []
    for word in (in_str.split()):
        a = word[::2].upper()
        b = word[1::2].lower()
        new_word=''
        for i in range(len(b)):
            new_word+=a[i]+b[i]
        if (len(a)>len(b)):
            new_word+=a[-1]
        print(new_word)
        lst.append(new_word)
    out_str = " ".join(lst)
    return out_str

# 2
def to_weird(in_str):
    lst = []
    for word in (in_str.split()):
        new_word=''
        for i in range(len(word)):
            if i%2==0:
                new_word+=word[i].upper()
            else: new_word+=word[i].lower()

        lst.append(new_word)
    out_str = " ".join(lst)
    return out_str

print(to_weird(L))

