def array_to_set(nums: list) -> list:
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
    return [x] + array_to_set(zs + ys)