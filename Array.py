# # import array
# # import array as arr
from array import *
#
# # a1 = array.array('i',[1,2,3,4])
# # print(a1)
# #
# # a2 = arr.array('i',[1,2,3,4])
# # print(a2)
#
# a3 = array('i',[1,2,3,4])
# print(a3)
#
# print(a3[1])
#
# print(len(a3))
#
# a3.append(5)
# print(a3)
#
# a3.extend([6,7,9,10])
# print(a3)
#
# a3.insert(7,8)
# print(a3)
#
# a3.pop()#it will return the value
# print(a3)
#
# a3.pop(0)
# print(a3)
#
# a3.pop(-1)
# print(a3)
#
# a3.remove(8) #it will not return anytjing
# print(a3)

a = array('i',[1,2,3,4,5])
b = array('i',[1,2,3,4,5,6,7,8,9,10])

#Array Concatination
c = array('i')
c = a + b
print(c)

#Array Slicing
print(c[0:5])
print(c[0:-2])

#Array Reversing
print(c[::-1])


