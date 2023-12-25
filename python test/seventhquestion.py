def sum_except_min_max(arr):
    return sum(filter(lambda num: num != min(arr) and num != max(arr), arr))


arr = [1, 4, 7, 1,2]
result = sum_except_min_max(arr)
print(result)