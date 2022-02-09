from collections import ChainMap

list1 = {1: 'a', 2: 'k', 3: 'a', 4: 's', 5: 'h'}

list2 = {6: 'b', 7: 'g'}

list3 = ChainMap(list1,list2)
print(list3)