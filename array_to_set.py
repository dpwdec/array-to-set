from typing import List

def array_to_sets(arr: List) -> List:
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