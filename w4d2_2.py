def get_min_max(lst):
    return min(lst), max(lst)

numbers = [3, 7, 1, 9, 4]
mn, mx = get_min_max(numbers)
print("최소값:", mn)
print("최대값:", mx)