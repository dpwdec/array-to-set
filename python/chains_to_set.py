from typing import List, Set

# REDUNDANT NOW, old solution for getting unique element ordered array

def array_to_sets(arr: List) -> List[Set]:
    return chain_to_sets(array_to_sets(arr))

# run time efficient solution
# function assumes array is sorted
def array_to_chain(nums: List[int]) -> List[int]:
    if len(nums) <= 2: return nums

    # destructure array
    x, *xs = nums

    # split array into two sections on different elements
    ys = [y for y in xs 
            if y == x]

    zs = xs[len(ys):]

    # switch array by
    # putting elements of array that match x to end
    # recursive call
    return [x] + array_to_chain(zs + ys)

def chain_to_sets(arr):
    s = set()
    sets = []
    for x in arr:
        if x not in s:
            s.add(x)
        else:
            sets.append(s)
            s = set([x])
    
    return sets

print(chain_to_sets([1, 2, 3, 1]))