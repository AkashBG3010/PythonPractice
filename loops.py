list = [1,2,3,4,5,6,7]

for value in list:
	print(value)


list = [1,2,3,4,5,6,7...20]
sum = 0
for value in list:
	sum = sum + value
	print(sum)


range(5) //// 0,1,2,3,4
range(10,100)//// 10,11,12,13,14,15,16,17.....100
range(10,100,5)//// 10,15,20,25,30,35....100



for value in range(1,10):
	print(value)


sum = 0
for value in range(1,21):
	sum = sum + value

print(sum)


l = [10,20,30,40]
key = 400

for value in l:
	if value == key:
		print("Element found")
		break
	else:
		continue
else:
	print("Element not found")
	


l = [10,20,30,40]
key = 40

for index,value in enumerate(l):
	# print(index,value)
	if value == key:
		print("Element if found at index",index)
		break
	else:
		continue
else:
	print("Element not found")
