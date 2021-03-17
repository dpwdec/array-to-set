from typing import List, Set

# simplest recursive solution
# requires mutating arrays and sets
def array_to_sets(arr: List) -> List[Set]:
    s = set()
    for x in arr:
        if x not in s:
            s.add(x)
    
    for x in s:
        arr.remove(x)
    
    if len(arr) == 0:
        return [s]
    else:
        return [s] + array_to_sets(arr)