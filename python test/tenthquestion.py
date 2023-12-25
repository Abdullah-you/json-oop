strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"]
list1 = []
N = 2
for i in range(len(strarr)):
    if len(strarr) >= N:
        list1.append("".join(strarr[:N]))
        strarr.pop(0)
    else:
        break
print(list1)

lengths = [len(s) for s in list1]
highest_index = lengths.index(max(lengths))
longest_string = list1[highest_index]
print(longest_string)

