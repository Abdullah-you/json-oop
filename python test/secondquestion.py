#from collections import Counter

#a = ["bcdef","abcdefg","bcde","bcdef"]
#res = Counter(a)
#print(res)

#print(f"{len(res.keys())}")
#for key, value in res.items():
#   print(f"{value}", end=" ")


a = ["bcdef", "abcdefg", "bcde","bcdef"]
list1 = []
list2 = []
for i in a:
    if i not in list1:
        list1.append(i)
print(len(list1))
for i in a:
    count = 0
    var = i
    if i in list2:
        continue
    for k in a:
        if var == k:
            count += 1
            continue
        else:
            continue
    list2.append(i)
    print(count, end=" ")

   


        