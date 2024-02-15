def first_version_naive(sort_this):
    list_len = len(sort_this)
    count = 0
    for i in range(list_len):
        for j in range (i+1, list_len):
            count += 1
            if sort_this[i]>sort_this[j]:
                bigger = sort_this[i]
                sort_this[i] = sort_this[j]
                sort_this[j] = bigger
    return sort_this, count


def unoptimized_but_better(sort_this):
    list_len = len(sort_this)
    count = 0
    for i in range(list_len-1):
        for j in range (list_len-i-1):
            count += 1
            if sort_this[j]>sort_this[j+1]:
                sort_this[j], sort_this[j+1] = sort_this[j+1], sort_this[j]
    return sort_this, count


def optimized_bubble_sort(sort_this):
    list_len = len(sort_this)
    count = 0
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements

    # range(list_len) also work but outer loop will
    # repeat one time more than needed.
    # Last i elements are already in place
    for i in range(list_len-1):
        for j in range(list_len-i-1):
            count += 1
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if sort_this[j]>sort_this[j+1]:
                swapped = True
                sort_this[j], sort_this[j+1] = sort_this[j+1], sort_this[j]

            if not swapped:
                # if we haven't needed to make a single swap in inner loop,
                # we can just exit the main loop.
                return sort_this, count
    return sort_this, count



if __name__ == '__main__':
    sort_this = [7, 4, 0, 3, 6, 1, 2, 5, 9, 8]
    sorted_, attempts_ = first_version_naive(sort_this)
    print("sorted list : ", sorted_)
    print(f"list was parsed {attempts_} times")

    s1, a1 = unoptimized_but_better(sort_this)
    print("sorted list : ", s1)
    print(f"list was parsed {a1} times")

    s2, a2 = optimized_bubble_sort(sort_this)
    print("sorted list : ", s2)
    print(f"list was parsed {a2} times")

    sort_this = [5, 1, 4, 2, 8]
    sorted_, attempts_ = first_version_naive(sort_this)
    print("sorted list : ", sorted_)
    print(f"list was parsed {attempts_} times")

    s1, a1 = unoptimized_but_better(sort_this)
    print("sorted list : ", s1)
    print(f"list was parsed {a1} times")

    s2, a2 = optimized_bubble_sort(sort_this)
    print("sorted list : ", s2)
    print(f"list was parsed {a2} times")