def get_count(sentence):
    count = 0
    for character in sentence:
        if character in 'aeiou':
            count += 1
        else:
            continue
    return count
string = 'abracadabra'
ans = get_count(string)
print(ans)

     