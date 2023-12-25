def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

n = int(input("Enter lenght of Finonacci: "))
list1 = fibonacci_sequence(n)
print(list1)

a = map(lambda x: x**3, list1)
print(list(a))

# a = ["bcdef", "abcdefg", "bcde","bcdef", "ali", "abdullah", "bcde","bcdef"]
# list1 = []
# list2 = []
# for i in a:
#     if i not in list1:
#         list1.append(i)
# print(len(list1))
# for i in a:
#     count = 0
#     var = i
#     if i in list2:
#         continue
#     for k in a:
#         if var == k:
#             count += 1
#             continue
#         else:
#             continue
#     list2.append(i)
#     print(count, end=" ")
#print(list1)














        

    




