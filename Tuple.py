from collections import namedtuple

title = namedtuple('Courses', 'Name, Technology')
# details = title('Data Science','Python')
details = title._make(['Artificial Intelligence', 'Python'])
print(details)