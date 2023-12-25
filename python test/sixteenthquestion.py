a = "camelCase"
list1 = list(a)

index_list = []
for i in list1:
    if i.isupper():
        ind = list1.index(i)
        index_list.append(ind)
    else:
        pass
    
k = 0
for j in index_list:
    list1.insert(j+k, " ")
    k+=1

answer = "".join(list1)
print(answer)
