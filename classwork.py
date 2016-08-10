def convert(word):
    out = ''
    for s in word:
        if s.isalpha():
            out+=s
    return out

def autocomplete(strg, lst):
    out = [convert(word) for word in lst if word.startswith(convert(strg))]
    return out[0:5]


l = ['apple', 'grape', 'airport']

ai = autocomplete('ai', l)
print(ai)

