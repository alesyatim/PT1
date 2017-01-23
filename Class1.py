def fn():
    l = 'A'
    while True:
        l *= 2
        if len(l) > 1000:
            break
        yield l

gen = fn()
print(gen)

counter = 0
for letter in gen:
    print(letter)
    counter += 1
    if counter > 5:
        break

# print(gen.next())


dict([ [1,2], [2,3], (4,5)])

a = "AB"
b = {'1':'c', '2':'e'}
print(zip(a,b))

print(" ".join("ddd"))

