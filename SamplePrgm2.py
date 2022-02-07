numbers = (1,2,3,4,5,6,7,8,9)

even_count = 0;
odd_count = 0;

for value in numbers:
	if value%2 == 0:
		even_count+=1
	else:
		odd_count+=1
else:
	print("Total number of even numbers:",even_count)
	print("Total number of odd numbers:",odd_count)