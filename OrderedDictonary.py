from collections import OrderedDict

d = OrderedDict()
d[1] = 'a'
d[2] = 'k'
d[3] = 'a'
d[4] = 's'
d[5] = 'h'

print(d)

d[1] = 'A'
print(d)