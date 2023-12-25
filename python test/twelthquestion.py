input = "is2 Thi1s T4est 3a"

def find_number(word):
    for character in word:
        if character.isdigit():
            return int(character)
    return None

def sequence(sentence):
    words = sentence.split()
    sorted_words = sorted(words, key=find_number)
    return " ".join(sorted_words)

print(sequence(input))