import random
# list = [1,2,3,4,5,6,7]
#
# for value in list:
# 	print(value)
#
#
# list = [1,2,3,4,5,6,7...20]
# sum = 0
# for value in list:
# 	sum = sum + value
# 	print(sum)
#
#
# range(5) //// 0,1,2,3,4
# range(10,100)//// 10,11,12,13,14,15,16,17.....100
# range(10,100,5)//// 10,15,20,25,30,35....100
#
#
#
# for value in range(1,10):
# 	print(value)
#
#
# sum = 0
# for value in range(1,21):
# 	sum = sum + value
#
# print(sum)
#
#
# l = [10,20,30,40]
# key = 400
#
# for value in l:
# 	if value == key:
# 		print("Element found")
# 		break
# 	else:
# 		continue
# else:
# 	print("Element not found")
#
#
#
# l = [10,20,30,40]
# key = 40
#
# for index,value in enumerate(l):
# 	# print(index,value)
# 	if value == key:
# 		print("Element if found at index",index)
# 		break
# 	else:
# 		continue
# else:
# 	print("Element not found")


# #For loop----->

# list = [1,2,3,4,5,6,7]
#
# for x in list:
# 	print(x)
# print('-----------------------------------------')
# # #While loop----->
#
# temp = 0
# while temp < list[4]:
# 	print(list[temp])
# 	temp = temp + 1


# #While Loop------------------------------->

# count = 0
#
# while count <= 5:
# 	print("Number:", count)
# 	count += 1
# print("End of Program")
#////////////////////////////////////////

# n= 20
# to_be_guessed = int(n * random.random()) + 1
# guess = 0
# while guess != to_be_guessed:
# 	guess = int(input("New number: "))
# 	if guess > 0:
# 		if guess > to_be_guessed:
# 			print("Number is too large")
# 		elif guess < to_be_guessed:
# 			print("Number is too small")
# 	else:
# 		print("Sorry that you gave up!")
# 		break
# else:
# 	print("Congratulations, You won!")
# #////////////////////////////////////////////////////////
# fruits = ['Mango', 'Grapes', 'Apple']
#
# for fruit in fruits:
# 	print("fruit: ",fruit)
# print("End of program")
#
# #////////////////////////////////////////////////////////

#
# num = int(input("Number: "))
# factorial = 1
#
# if num < 0:
# 	print("Number Must be Possitive")
# elif num == 0:
# 	print("factorial = 0")
# else:
# 	for i in range(1,num+1):
# 		factorial = factorial * i
# print("factorial =", factorial)
# #////////////////////////////////////////////////////////


