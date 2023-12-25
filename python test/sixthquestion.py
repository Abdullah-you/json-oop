a = [2,2,2,2,-5,-10]

def positive_sum(input):
    print(sum([max(0, num) for num in input]))

positive_sum(a)