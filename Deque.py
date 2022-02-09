from collections import deque

list1 = ['a','k','a','s','h']
list2 = deque(list1)
print(list2)

list2.append('bg')
print(list2)

list2.appendleft('bg')
print(list2)

list2.pop()
print(list2)

list2.popleft()
print(list2)