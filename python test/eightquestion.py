
s = 'This is an example!'
def reverse(a):
    reversed_string = ""
    for words in s.split(' '):
        if reversed_string != '':
            reversed_string += " "
        for i in reversed(words):
            reversed_string += i
    print(reversed_string)
reverse(s)
