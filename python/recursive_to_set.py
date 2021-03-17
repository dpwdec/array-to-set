from typing import List, Set

# entirely recursive solution with no mutability
def array_to_sets(arr: List) -> List[Set]:
    zet = build_set(arr)

    banned = remove_once(arr, [ban for ban in zet])

    if len(banned) > 0:
        return [zet] + array_to_sets(banned)
    
    return [zet]

def build_set(arr: List) -> Set:
    if len(arr) == 1:
        return set(arr)

    x, *xs = arr

    return set([x]) | build_set(xs)

def remove_once(arr: List, ban: List) -> List:
    if len(arr) == 1:
        return [x for x in arr if x not in ban]
    
    x, *xs = arr

    if x in ban:
        return remove_once(xs, [b for b in ban if b != x])
    
    return [x] + remove_once(xs, ban)
