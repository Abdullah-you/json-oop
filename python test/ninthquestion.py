a = 'test'
if (len(a)%2==0):
    list1 = list(a)
    index = len(list1)//2-1 
    ind1 = str(list1[index])
    ind2 = str(list1[index+1])
    print(f"{ind1}{ind2}")
else:
    list1 = list(a)
    index = len(list1) // 2
    print(list1[index])