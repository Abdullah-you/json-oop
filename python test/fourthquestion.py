a = '1222311'
def consecutive_occurrences(string):
    replaced_string = ""
    count = 0
    prev_char = ""

    for char in string:
        if char == prev_char:
            count += 1
        else:
            if count > 0:
                replaced_string += f"({count}, {prev_char})"
            count = 1
            prev_char = char
            #replaced_string += char
    
    if count > 0:
        replaced_string += f"({count}, {prev_char})"
    
    print(replaced_string)

consecutive_occurrences(a)