l = [1, 2]
l2 = [3]
for x, y in zip(l, l2):
	print(x)
# ah, as I suspected, when zip() two lists, if one shorter than the other, then cut of the rest from the longer one


