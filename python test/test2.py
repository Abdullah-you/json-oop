# def find_outlier(integers):
#     odds = [i for i in integers if i % 2 != 0]
#     evens = [i for i in integers if i % 2 == 0]
#     return odds[0] if len(odds) == 1 else evens[0]


# [2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

# [160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)

def find_outlier(integers):
	evens = []
	odds = []
	for each in integers:
		if each%2==0:
			evens.append(each)
		else:
			odds.append(each)
		if len(evens)>1 and len(odds)==1:
			return odds[0]
		elif len(odds)>1 and len(evens)==1:
			return evens[0]
a = [2, 4, 0, 100, 4, 11, 2602, 36]
ans = find_outlier(a)
print(ans)