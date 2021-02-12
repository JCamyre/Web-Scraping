dic = {}
dic['years'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for key, val in dic.items():
# 	for vals in val:
# 		print(f'{key}: {vals}')

for x, y in enumerate(dic.items()):
	y, z = y
	print(x, y, z)
print(dic.items())