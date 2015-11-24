def add(a, b, res = None):
    if res is None:
        res = []
    r = a + b
    res.append(r)
    print(res)
    return r

add(1,2)
add(2,3)
add(4,5)
