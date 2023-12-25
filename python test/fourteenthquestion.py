string = 'ABBCcAD'
new_list = []
for i in string:
    if not new_list:
             new_list.append(i)
    elif new_list[-1] != i:
             new_list.append(i)
print(str(new_list))