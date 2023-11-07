def mult_list(*list):
    if len(list) == 0:
        return 0 
    
    prod = list[0]

    if len(list) > 1:
        for i in list[1:]:
            prod = prod * i

    return prod

print(mult_list(2,2,2))