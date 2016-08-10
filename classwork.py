def convert(word):
    return ''.join((s for s in word if s.isalpha()))

def autocomplete(strg, lst):
    return [convert(word) for word in lst if word.startswith(convert(strg))][0:5]


l = ['apple', 'grape', 'airport']

ai = autocomplete('ai', l)
print(ai)


print(convert('kjak 6$jk76'))
