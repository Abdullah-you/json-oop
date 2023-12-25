def digital_root(n):
    #list2 = []
    list1 = list(str(n))
    sum = 0
    add = 0 
    for num in list1:
        sum += int(num)
    #list2.append(sum)
    var = sum
    while var >= 10:
        list2 = list(str(var))
        add = 0
        for i in list2:
            add += int(i)
            var = add
    return var
    
number = 45676
ans = digital_root(number)
print(ans)