def num_within(num, r, end_range):
    return num in range(r, end_range+1)

print(num_within(3,2,4))     
print(num_within(3,1,3))     
print(num_within(10,2,5))