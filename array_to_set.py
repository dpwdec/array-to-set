

def array_to_set(nums: list) -> list:
    # destructure array
    x, *xs = nums

    ys = simple_split(xs)

    zs = xs[:len(ys)]

    return [x + array_to_set(zs + ys)]

def split_array(a: list):
    x, y, *xs = a
    if x == y:
        return [x] + split_array([y] + xs)
    else:
        return [x]

def split_array_2(a: list):
    goodvals = [1]
    good, bad = [], []
    for x in a:
        (bad, good)[x in goodvals].append(x)
    return [good, bad]

def split_array_3(a: list):
    x, *xs = a
    return [[y for y in a if y in [x]], [y for y in a if not y in [x]]]

# g = [1, 1, 2, 3, 4, 5, 6]

# gs = split_array(g)

# hs = g[len(gs):]

# print([gs, hs])

print(split_array_2([1, 1, 1, 2, 3, 4]))