def max_num(*int):
    arr = []
    for item in int:
        arr.append(item)
    return max(arr)

print(max_num(1,2,3,4,5))