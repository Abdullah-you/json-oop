import string

def seperate(grid):
    alphanumeric_chars = set(string.ascii_letters + string.digits)
    decoded = ''.join(''.join(c for c in col if c in alphanumeric_chars) for col in zip(*grid))
    return decoded

input = [
    "Tsi",
    "h%x",
    "i #",
    "sM ",
    "$a ",
    "#t%",
    "ir!"
]

output = seperate(input)
print(output)