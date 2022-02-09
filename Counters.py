from collections import Counter

a = [1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,5,6,6,7]
c = Counter(a)
print(c)

print(list(c.elements()))

print(c.most_common())

sub = {2:1 , 6:1}
print(c.subtract(sub))
print(c.most_common())