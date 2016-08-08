a = [[1,2],(3,4), {6: [10, 16]}]

def unwrap(x):
    if len(x):
        for _ in x:
            unwrap(_)
    else: print(x)

    '''
    try:
        for item in x:
            unwrap(x)
        return
    except:
        print(x)
        return x
    '''
unwrap(a)