
L = '''The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

email = 'alesya_tim@tut.by'
# Concatenate L and email
L+=email

length = len(L)
print('length L = ', length)

# Vowels: y  sometimes represents a vowel and sometimes a consonant. Let it be a vowel
vowels='aeyuio'
count_vowels=0
pos=1 # counter
for s in L:
    if s in vowels:
        count_vowels+=1
    if pos%18 == 0:
        print(pos,s.swapcase())
    pos+=1

print('Count of all vowels = ', count_vowels)